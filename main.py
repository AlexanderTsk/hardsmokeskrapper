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
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-420/420-light-100-g"  
    # start_model = 10001
    # price = 295
    # manufacturer_id = 17
    # сategories_ids = [59, 64, 78]
    # name_regex=r"^Тютюн 420 Light"

    #Data for Tobacco 420 Classic (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-420/420-tobacco-100-g"  
    # start_model = 10131
    # price = 320
    # manufacturer_id = 17
    # сategories_ids = [59, 64, 79]
    # name_regex=r"^Тютюн 420"

    #Data for Tobacco Custom (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-custom/custom-100-g"  
    # start_model = 10137
    # price = 335
    # manufacturer_id = 18
    # сategories_ids = [59, 65, 80]
    # name_regex=r"^Тютюн Custom"

    #Data for Dead Horse (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-dead-horse/dead-horse-100g"  
    # start_model = 10149
    # price = 450
    # manufacturer_id = 19
    # сategories_ids = [59, 66, 81]
    # name_regex=r"^Тютюн Dead Horse"

    #Data for Pixtea (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/kalyannaya-chaynaya-smes-pixtea/pixtea-50-g"  
    # start_model = 10193
    # price = 120
    # manufacturer_id = 30
    # сategories_ids = [59, 105, 106]
    # name_regex=r"^Кальянна чайна суміш Pixtea"

    #Data for Turbo (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-turbo/turbo-100-g"  
    # start_model = 10212
    # price = 340
    # manufacturer_id = 31
    # сategories_ids = [59, 107, 108]
    # name_regex=r"^Тютюн Turbo"

    #Data for Yummy (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-yummy/yummy-100g"  
    # start_model = 10236
    # price = 295
    # manufacturer_id = 14
    # сategories_ids = [59, 67, 82]
    # name_regex=r"^Тютюн Yummy"

    #Data for Cult Light (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-cultt/cultt-100-g"  
    # start_model = 10266
    # price = 390
    # manufacturer_id = 20
    # сategories_ids = [59, 68, 83]
    # name_regex=r"^Тютюн CULTt"

    #Data for Cult Medium (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-cultt/cultt-medium-100-g"  
    # start_model = 10356
    # price = 390
    # manufacturer_id = 20
    # сategories_ids = [59, 68, 84]
    # name_regex=r"^Тютюн CULTt Medium"

    #Data for Cult Strong (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-cultt/cultt-strong-100-g"  
    # start_model = 10415
    # price = 445
    # manufacturer_id = 20
    # сategories_ids = [59, 68, 85]
    # name_regex=r"^Тютюн CULTt Strong"

    #Data for Space Tea (40g)
    # data_url = "https://hardsmoke.store/katalog/tabak/kalyannaya-smes-space-tea/space-tea-40g"  
    # start_model = 10474
    # price = 135
    # manufacturer_id = 32
    # сategories_ids = [59, 109, 110]
    # name_regex=r"^Кальянна чайна суміш Space Tea"

    #Data for Creepy (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-creepy/creepy-100g"  
    # start_model = 10521
    # price = 360
    # manufacturer_id = 11
    # сategories_ids = [59, 69, 86]
    # name_regex=r"^Тютюн Creepy"

    #Data for Jibiar (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-jibiar/jibiar-50-g"  
    # start_model = 10553
    # price = 150
    # manufacturer_id = 21
    # сategories_ids = [59, 87, 88]
    # name_regex=r"^Тютюн Jibiar"

    #Data for Unity (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-unity/unity-100-g"  
    # start_model = 10707
    # price = 370
    # manufacturer_id = 13
    # сategories_ids = [59, 70, 89]
    # name_regex=r"^Тютюн Unity"

    #Data for Molfar Chill Line (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-molfar/molfar-chill-line-100-g"  
    # start_model = 10756
    # price = 295
    # manufacturer_id = 23
    # сategories_ids = [59, 71, 90]
    # name_regex=r"^Тютюн Molfar Chill Line"

    #Data for Molfar Spirit Line (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-molfar/molfar-spirit-line-100-g"  
    # start_model = 10789
    # price = 350
    # manufacturer_id = 23
    # сategories_ids = [59, 71, 91]
    # name_regex=r"^Тютюн Molfar Spirit Line"

    #Data for Molfar Virginia Line (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-molfar/molfar-virginia-line-100-g"  
    # start_model = 10811
    # price = 280
    # manufacturer_id = 23
    # сategories_ids = [59, 71, 92]
    # name_regex=r"^Тютюн Molfar Virginia Line"

    #Data for Heven (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-heven/heven-50-g"  
    # start_model = 10849
    # price = 220
    # manufacturer_id = 24
    # сategories_ids = [59, 93, 94]
    # name_regex=r"^Тютюн Heven"
    
    #Data for Spam (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-spam/spam-100-g"  
    # start_model = 10877
    # price = 310
    # manufacturer_id = 25
    # сategories_ids = [59, 72, 95]
    # name_regex=r"^Тютюн Spam"

    #Data for Swipe (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/kalyannaya-smes-swipe/swipe-50-g"  
    # start_model = 10907
    # price = 110
    # manufacturer_id = 26
    # сategories_ids = [59, 73, 96]
    # name_regex=r"^Кальянна суміш Swipe"

    #Data for Swipe (100g)
    # data_url = "https://hardsmoke.store/katalog/tabak/kalyannaya-smes-swipe/swipe-100-g"  
    # start_model = 10954
    # price = 175
    # manufacturer_id = 26
    # сategories_ids = [59, 73, 111]
    # name_regex=r"^Кальянна суміш Swipe"

    #Data for Loud (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-loud/loud-light-50-g"  
    # start_model = 11002
    # price = 150
    # manufacturer_id = 27
    # сategories_ids = [59, 74, 97]
    # name_regex=r"^Тютюн Loud"

    #Data for Buta (50g)
    # data_url = "https://hardsmoke.store/katalog/tabak/tabak-dlya-kalyana-buta/buta-gold-50-g"  
    # start_model = 11032
    # price = 115
    # manufacturer_id = 33
    # сategories_ids = [59, 98, 99]
    # name_regex=r"^Тютюн Buta"

    # #Data for 420 liquids (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/ridyny-420-liquid/420-liquid-50-mg-30-ml"  
    # start_model = 11157
    # price = 360
    # manufacturer_id = 17
    # сategories_ids = [60, 77, 100, 101]
    # name_regex=r"^Рідина 420 Liquid"

    #Data for 420 liquids (50mg 10ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/ridyny-420-liquid/420-liquid-50-mg-10-ml"  
    # start_model = 11179
    # price = 160
    # manufacturer_id = 17
    # сategories_ids = [60, 77, 100, 102]
    # name_regex=r"^Рідина 420 Liquid"

    #Data for Alchemist liquids (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/zhidkosti-alchemist/alchemist-50mg"  
    # start_model = 11201
    # price = 380
    # manufacturer_id = 15
    # сategories_ids = [60, 77, 103, 104]
    # name_regex=r"^Рідина Alchemist Salt"

    #Data for Alchemist liquids (50mg 10ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/zhidkosti-alchemist/alchemist-50-mg"  
    # start_model = 11219
    # price = 170
    # manufacturer_id = 15
    # сategories_ids = [60, 77, 103, 112]
    # name_regex=r"^Рідина Alchemist Salt"

    #Data for charcoals Gresko
    # data_url = "https://hardsmoke.store/katalog/ugli/orehovyiy-ugol-dlya-kalyana-gresco"  
    # start_model = 11237
    # price = 200
    # manufacturer_id = 39
    # сategories_ids = [62, 137]
    # name_regex=r"^Горіхове вугілля для кальяну Gresco"


    # #Data for charcoals Cocoloco
    # data_url = "https://hardsmoke.store/katalog/ugli/kokosovyj-ugol-dlya-kalyana-cocoloco"  
    # start_model = 11246
    # price = 300
    # manufacturer_id = 40
    # сategories_ids = [62, 138]
    # name_regex=r"^Кокосове вугілля для кальяну Cocoloco"

    #Data for charcoals Garden
    # data_url = "https://hardsmoke.store/katalog/ugli/kokosovyiy-ugol-dlya-kalyana-garden"  
    # start_model = 11250
    # price = 210
    # manufacturer_id = 38
    # сategories_ids = [62, 139]
    # name_regex=r"^Кокосове вугілля для кальяну Garden"

    #Data for Hype Liquid Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/hype/nabory-dlya-samozamesa-hype-kit-50-mg-30-ml"  
    # start_model = 11252
    # price = 320
    # manufacturer_id = 36
    # сategories_ids = [60, 76, 128, 129]
    # name_regex=r"^Набір для самозамішування Hype Kit"

    #Data for Punch Liquid Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/jidkosti-punch/nabor-dlya-samozamesa-punch-50-mg-30-ml"  
    # start_model = 11286
    # price = 399
    # manufacturer_id = 37
    # сategories_ids = [60, 76, 130, 131]
    # name_regex=r"^Набір для самозамішування Punch"

    #Data for Punch Lucky Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/lucky/nabory-dlya-samozamesa-lucky-50-mg-30-ml"  
    # start_model = 11306
    # price = 360
    # manufacturer_id = 35
    # сategories_ids = [60, 76, 135, 136]
    # name_regex=r"^Набір для самозамішування Lucky"

    #Data for Chaser Black Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/chaser/chaser-black-50-mg-30-ml"  
    # start_model = 11343
    # price = 330
    # manufacturer_id = 16
    # сategories_ids = [60, 76, 132, 134]
    # name_regex=r"^Набір для самозамішування Chaser Black"

    #Data for Chaser for PODs Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/chaser/chaser-for-pods-50-mg-30-ml"  
    # start_model = 11364
    # price = 330
    # manufacturer_id = 16
    # сategories_ids = [60, 76, 132, 133]
    # name_regex=r"^Набір для самозамішування Chaser"

    #Data for Alchemist Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/alchemist/alchemist-50-mg-30-ml"  
    # start_model = 11396
    # price = 360
    # manufacturer_id = 15
    # сategories_ids = [60, 76, 147, 148]
    # name_regex=r"^Набір для самозамішування Alchemist Salt"

    #Data for Alchemist Kit (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/nabory-dlya-samozamesa/alchemist/alchemist-50-mg-30-ml"  
    # start_model = 11396
    # price = 360
    # manufacturer_id = 15
    # сategories_ids = [60, 76, 147, 148]
    # name_regex=r"^Набір для самозамішування Alchemist Salt"

    #Data for Cartridge Geekvape
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-geekvape"  
    # start_model = 11414
    # price = 130
    # manufacturer_id = 41
    # сategories_ids = [61, 141]
    # name_regex=r"^Картридж Geekvape"


    #Data for Cartridge Lost Vape
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-lost-vape"  
    # start_model = 11420
    # price = 130
    # manufacturer_id = 42
    # сategories_ids = [61, 142]
    # name_regex=r"^Картридж Lost vape"

    #Data for Cartridge Oxva
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-oxva"  
    # start_model = 11423
    # price = 152
    # manufacturer_id = 43
    # сategories_ids = [61, 143]
    # name_regex=r"^Картридж OXVA"

    #Data for Cartridge Vaporesso
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-vaporesso"  
    # start_model = 11427
    # price = 139
    # manufacturer_id = 44
    # сategories_ids = [61, 144]
    # name_regex=r"^Картридж Vaporesso"

    #Data for Cartridge Voopoo
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-voopoo"  
    # start_model = 11445
    # price = 152
    # manufacturer_id = 45
    # сategories_ids = [61, 145]
    # name_regex=r"^Картридж Voopoo"

    #Data for Cartridge Elfbar
    # data_url = "https://hardsmoke.store/katalog/kartridji-ispariteli/kartridzhi/kartridzhi-elf-bar"  
    # start_model = 11456
    # price = 132
    # manufacturer_id = 12
    # сategories_ids = [61, 140]
    # name_regex=r"^Картридж Elf Bar ELFX"

    #Data for Elfbar 1500
    # data_url = "https://hardsmoke.store/katalog/esigareti/odnorazovye/odnorazki-elf-bar/elf-bar-1500"  
    # start_model = 11458
    # price = 400
    # manufacturer_id = 12
    # сategories_ids = [146, 149]
    # name_regex=r"^Elf Bar 1500"

    #Data for Elfbar TE6000
    # data_url = "https://hardsmoke.store/katalog/esigareti/odnorazovye/odnorazki-elf-bar/odnorazovyie-elektronnyie-sigaretyi-pod-elf-bar-te6000"  
    # start_model = 11496
    # price = 600
    # manufacturer_id = 12
    # сategories_ids = [146, 150]
    # name_regex=r"^Elf Bar TE6000"

    #Data for Elfbar GH23000
    # data_url = "https://hardsmoke.store/katalog/esigareti/odnorazovye/odnorazki-elf-bar/odnorazovyie-elektronnyie-sigaretyi-pod-elf-bar-gh-23000"  
    # start_model = 11533
    # price = 850
    # manufacturer_id = 12
    # сategories_ids = [146, 151]
    # name_regex=r"^Elf Bar GH 23000"

    #Data for Elfbar Ice King 30000
    # data_url = "https://hardsmoke.store/katalog/esigareti/odnorazovye/odnorazki-elf-bar/odnorazovyie-elektronnyie-sigaretyi-pod-elf-bar-ice-king-30000"  
    # start_model = 11557
    # price = 950
    # manufacturer_id = 12
    # сategories_ids = [146, 152]
    # name_regex=r"^Elf Bar Ice King 30000"

    #Data for Elfliq (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-elfliq/elfliq-30ml"  
    # start_model = 11572
    # price = 350
    # manufacturer_id = 29
    # сategories_ids = [60, 77, 113, 114]
    # name_regex=r"^Рідина Elfliq"

    #Data for Elfliq (50mg 10ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-elfliq/elfliq-10ml"  
    # start_model = 11622
    # price = 165
    # manufacturer_id = 29
    # сategories_ids = [60, 77, 113, 115]
    # name_regex=r"^Рідина Elfliq"

    #Data for Creepy (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/zhidkosti-creepy/creepy-50-mg-30-ml"  
    # start_model = 11670
    # price = 300
    # manufacturer_id = 11
    # сategories_ids = [60, 77, 116, 117]
    # name_regex=r"^Рідина Creepy"

    #Data for Katana (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-eight-by-katana/katana-30ml"  
    # start_model = 11697
    # price = 460
    # manufacturer_id = 34
    # сategories_ids = [60, 77, 118, 119]
    # name_regex=r"^Рідина Eight by Katana"

    #Data for Lucky (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-lucky/lucky-30-ml"  
    # start_model = 11779
    # price = 350
    # manufacturer_id = 35
    # сategories_ids = [60, 77, 120, 121]
    # name_regex=r"^Рідина Lucky"

    #Data for Lucky (50mg 15ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-lucky/lucky-15-ml"  
    # start_model = 11809
    # price = 175
    # manufacturer_id = 35
    # сategories_ids = [60, 77, 120, 122]
    # name_regex=r"^Рідина Lucky"

    #Data for Yummy (50mg 30ml)
    # data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-yummy/yummy-50-mg-30-ml"  
    # start_model = 11839
    # price = 300
    # manufacturer_id = 14
    # сategories_ids = [60, 77, 123, 124]
    # name_regex=r"^Рідина YUMMY"

    #Data for Chaser for pods (50mg 30ml)
    data_url = "https://hardsmoke.store/katalog/zhidkosti/solevye/jidkosti-chaser/chaser-for-pods/chaser-50-mg-30-ml"  
    start_model = 11854
    price = 330
    manufacturer_id = 16
    сategories_ids = [60, 77, 125, 126, 127]
    name_regex=r"^Рідина Chaser"

    
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
