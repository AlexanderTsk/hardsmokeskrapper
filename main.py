import asyncio
from service.image_saver import ImageSaver
from db.connector import DbConnector
from oc_import import OcImport

async def main():

    connector = DbConnector(
        host="localhost",
        user="root",
        password="",
        database="altsmoke_db"
    )

    image_saver = ImageSaver("/Applications/XAMPP/xamppfiles/htdocs/altsmoke/image/catalog/product")

    #Data for Tobacco 420 Light (100g)
    data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-420/420-light-100-g"  
    start_model = 10001
    price = 295
    manufacturer_id = 17
    сategories_ids = [59, 64, 78]
    name_regex=r"^Тютюн 420 Light"
    
    oc_import = OcImport(connector, image_saver)
    await oc_import.importData(
        data_url=data_url,
        start_model=start_model,
        price=price,
        manufacturer_id=manufacturer_id,
        сategories_ids=сategories_ids,
        name_regex=name_regex
    )

       

if __name__ == "__main__":
    asyncio.run(main())
