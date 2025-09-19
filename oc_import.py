import asyncio
from browser import PlaywrightBrowser 

from db.connector import DbConnector
from db.product import Product
from entity.parsed_product import ParsedProduct
from service.normalizer import Normalizer
from service.image_saver import ImageSaver

class OcImport:

    def __init__(self, db_connector: DbConnector, image_saver: ImageSaver):
        self.db_connector = db_connector
        self.image_saver = image_saver

    async def importData(
        self,
        data_url: str,
        start_model: int, 
        price: float,
        manufacturer_id: int,
        сategories_ids: list[int],
        name_regex: str | None = None
    ):
        browser = PlaywrightBrowser(url=data_url, name_regex=name_regex)
        products: list[ParsedProduct] = await browser.parse()

        normalizer = Normalizer(self.db_connector, self.image_saver)
        product_db = Product(self.db_connector)

        model = start_model
        for product in products:
            stored_product = product_db.getProductByName(product.name)
            if stored_product == None:
                print("Adding new product: ", product.name)
                normalized_product = normalizer.normalize(
                    parsed_product=product,
                    model=model,
                    price=price,
                    manufacturer_id=manufacturer_id,
                    catrgories_ids=сategories_ids
                )
                new_product_id = product_db.addProduct(normalized_product)
                model +=1
            else:
                print(f"Product {product.name} already stored")
