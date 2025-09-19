from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ParsedProduct:
    name: str
    attributes: Dict[str, str]
    description: str
    image: str
    gallery: List[str]