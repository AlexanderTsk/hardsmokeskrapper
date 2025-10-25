import re
from string import Template
from bs4 import BeautifulSoup
from slugify import slugify

from entity.parsed_product import ParsedProduct
from entity.normalized_product import NormalizedProduct

from service.adapter import AttributeGroupAdapter, AttributeAdapter
from service.image_saver import ImageSaver

from db.connector import DbConnector
from db.attribute import Attribute

class Normalizer:

    def __init__(self, connectior: DbConnector, image_saver: ImageSaver):
        self.connector = connectior
        self.image_saver = image_saver

        self.meta_title_template = Template(
            "$name купити з доставкою в Україні | Alt Smoke"
        )
        self.meta_description_template = Template(
            "Купити $name в інтернет-магазині AltSmoke ✔️ Вигідна ціна ✔️ Швидка доставка по Україні"
        )
        self.meta_keywords_template = Template(
            "купити $name, Alt Smoke Україна, інтернет-магазин кальянів"
        )

    def normalize(
            self, 
            parsed_product: ParsedProduct,
            model: int,
            price: float,
            manufacturer_id:int,
            catrgories_ids: list[int]
            ) -> NormalizedProduct:
        ctx = {"name": parsed_product.name}

        meta_title = self.meta_title_template.safe_substitute(ctx)
        meta_description = self.meta_description_template.safe_substitute(ctx)
        meta_keywords = self.meta_keywords_template.safe_substitute(ctx)

        seo_url = slugify(parsed_product.name)

        attribute_group_atapter = AttributeGroupAdapter()
        attribute_adapter = AttributeAdapter()
        attribute_db = Attribute(self.connector)

        attribute_ids = []
      
        for attribute_group, attribues in parsed_product.attributes.items():
            attribut_group_name = attribute_group_atapter.adapt(attribute_group)
            internal_group = attribute_db.getAttributeGroupByName(attribut_group_name)
            if internal_group:
                attributes_list = attribues.split(',')
                for attribute in attributes_list:
                    attribute = attribute.strip()
                    internal_attribute = attribute_db.getAttributeByName(internal_group['attribute_group_id'], attribute_adapter.adapt(attribute))
                    if internal_attribute:
                        attribute_ids.append(internal_attribute['attribute_id'])
                    else:
                        try:
                            new_attribute_id = attribute_db.addAttribute(internal_group['attribute_group_id'], attribute)
                            attribute_ids.append(new_attribute_id)
                        except:
                            print(f"Failed to add attribute: {attribute}")

        soup = BeautifulSoup(parsed_product.description, "html.parser")
        for img in soup.find_all("img"):
            img.decompose()

        for a in soup.find_all("a"):
            a.unwrap()

        clean_description = soup.decode_contents()
        clean_description = re.sub(r"HardSmoke", "Alt Smoke", clean_description, flags=re.IGNORECASE)

        main_image_path = None
        try:
            if parsed_product.image:
                main_image_path = self.image_saver.save_image(parsed_product.image, f"product-{model}")
        except Exception as e:
            print(f"[WARN] Failed to store image for {parsed_product.name}: {e}")

        gallery_path = []
        for idx, image_url in enumerate(parsed_product.gallery, start=1):
            try:
                if image_url:
                    image_path = self.image_saver.save_image(image_url, f"product-{model}-gallery-{idx}")
                    gallery_path.append(image_path)
            except Exception as e:
                print(f"[WARN] Failed to store gallery image {idx} for {parsed_product.name}: {e}")



        return NormalizedProduct(
            name=str(parsed_product.name).strip(),
            description=clean_description,
            meta_title=str(meta_title).strip(),
            meta_description=str(meta_description).strip(),
            meta_keywords=str(meta_keywords).strip(),
            seo_url=seo_url,
            model=model,
            price=price,
            manufacturer_id=manufacturer_id,
            catrgories_ids=catrgories_ids,
            attribute_ids=attribute_ids,
            image_path=main_image_path,
            gallery_path=gallery_path
        )
