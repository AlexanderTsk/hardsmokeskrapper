from db.connector import DbConnector


class Attribute:

    def __init__(self, connector: DbConnector):
        self.connector = connector

    def getAttributeGroupByName(self, name: str, language_id: int = 2) -> dict | None:
        query = """
        SELECT ag.attribute_group_id, agd.name
        FROM oc_attribute_group ag
        JOIN oc_attribute_group_description agd
        ON ag.attribute_group_id = agd.attribute_group_id
        WHERE agd.name = %s AND agd.language_id = %s
        """
        self.connector.connect()
        result = self.connector.execute(query, (name, language_id))

        if result:
            row = result[0]
            return {
                "attribute_group_id": row[0],
                "name": row[1]
            }
        return None

    def getAttributeByName(self, attribute_group_id: int, name: str, language_id: int = 2) -> dict | None:
        query = """
        SELECT a.attribute_id, ad.name, a.attribute_group_id
        FROM oc_attribute a
        JOIN oc_attribute_description ad
        ON a.attribute_id = ad.attribute_id
        WHERE a.attribute_group_id = %s AND ad.name = %s AND ad.language_id = %s
        """
        self.connector.connect()
        result = self.connector.execute(query, (attribute_group_id, name, language_id))

        if result:
            row = result[0]
            return {
                "attribute_id": row[0],
                "name": row[1],
                "attribute_group_id": row[2]
            }
        return None

    def addAttribute(self, attribute_group_id: int, name: str, language_id: int = 2) -> int:
        self.connector.connect()

        insert_attribute_query = """
        INSERT INTO oc_attribute (attribute_group_id, sort_order)
        VALUES (%s, 0)
        """
        self.connector.execute(insert_attribute_query, (attribute_group_id,))
        attribute_id = self.connector.cursor.lastrowid

        insert_description_query = """
        INSERT INTO oc_attribute_description (attribute_id, language_id, name)
        VALUES (%s, %s, %s)
        """
        self.connector.execute(insert_description_query, (attribute_id, language_id, name))

        return attribute_id

    def addAttributeGroup(self, name: str, language_id: int = 1) -> int:
        self.connector.connect()

        insert_group_query = """
        INSERT INTO oc_attribute_group (sort_order)
        VALUES (0)
        """
        self.connector.execute(insert_group_query)
        attribute_group_id = self.connector.cursor.lastrowid

        insert_description_query = """
        INSERT INTO oc_attribute_group_description (attribute_group_id, language_id, name)
        VALUES (%s, %s, %s)
        """
        self.connector.execute(insert_description_query, (attribute_group_id, language_id, name))

        return attribute_group_id
