from db.connector import DbConnector
from entity.normalized_product import NormalizedProduct

class Product:

    def __init__(self, connector: DbConnector):
        self.connector = connector

    def getProductByName(self, name: str, language_id: int = 2):
      
        self.connector.connect()
        query = "SELECT product_id FROM oc_product_description WHERE name = %s AND language_id = %s"
        result = self.connector.execute(query, (name, language_id))
        return result[0][0] if result else None
    
    def addProduct(self, product: NormalizedProduct, language_id: int = 2):
        self.connector.connect()

        try:
            insert_product_query = """
            INSERT INTO oc_product
            (model, quantity, stock_status_id, manufacturer_id, price, date_available, minimum, status, image, date_added, date_modified)
            VALUES
            (%s, 1, 5, %s, %s, NOW(), 1, 1, %s, NOW(), NOW())
            """
            self.connector.execute(insert_product_query, (
                product.model,
                product.manufacturer_id,
                product.price,
                product.image_path
            ))
            product_id = self.connector.cursor.lastrowid

            # seo_url
            seo_url_query = """
                INSERT INTO oc_seo_url (language_id, `key`, `value`, keyword)
                VALUES (%s, %s, %s, %s)
            """
            self.connector.execute(seo_url_query, (language_id, 'product_id', product_id, product.seo_url))

            # description
            product_desc_query = """
            INSERT INTO oc_product_description
            (product_id, language_id, name, description, meta_title, meta_description, meta_keyword)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.connector.execute(product_desc_query, (
                product_id,
                language_id,
                product.name,
                product.description,
                product.meta_title,
                product.meta_description,
                product.meta_keywords
            ))

            # categories
            for category_id in product.catrgories_ids:
                self.connector.execute(
                    "INSERT INTO oc_product_to_category (product_id, category_id) VALUES (%s, %s)",
                    (product_id, category_id)
                )

            # attributes
            for attribute_id in product.attribute_ids:
                self.connector.execute(
                    "INSERT INTO oc_product_attribute (product_id, attribute_id, language_id, text) VALUES (%s, %s, %s, '')",
                    (product_id, attribute_id, language_id)
                )

            #gallery
            for idx, gallery_image_path in enumerate(product.gallery_path, start=1):
                self.connector.execute(
                    "INSERT INTO oc_product_image (product_id, image, sort_order) VALUES (%s, %s, %s)",
                    (product_id, gallery_image_path, idx)
                )

            #store
            product_store_query = """
            INSERT INTO oc_product_to_store
            (product_id, store_id)
            VALUES (%s, %s)
            """
            self.connector.execute(product_store_query, (
                product_id,
                0            
            ))

            self.connector.commit()

            return product_id

        except Exception as e:
            if self.connector.conn:
                self.connector.conn.rollback()
            raise e

