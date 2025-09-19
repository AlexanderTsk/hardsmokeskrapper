from dataclasses import dataclass

@dataclass
class NormalizedProduct:
    name: str
    description: str

    meta_title: str
    meta_description: str
    meta_keywords: str

    model: int
    price: float

    manufacturer_id: int

    catrgories_ids: list[int]
    attribute_ids: list[int]

    image_path: str
    gallery_path: list[str]

    seo_url: str