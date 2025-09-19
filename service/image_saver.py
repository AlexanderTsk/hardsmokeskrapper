import os
import requests
from PIL import Image
from io import BytesIO

class ImageSaver:
    def __init__(self, full_path: str, base_path: str = "catalog/product"):
        self.full_path = full_path
        self.base_path = base_path
        os.makedirs(self.full_path, exist_ok=True)

    def save_image(self, url: str, filename: str) -> str:
        filepath = os.path.join(self.full_path, f"{filename}.png")

        if os.path.exists(filepath):
            return os.path.join(self.base_path, f"{filename}.png")

        resp = requests.get(url, timeout=10)
        resp.raise_for_status()

        with Image.open(BytesIO(resp.content)) as img:
            img = img.convert("RGBA")

            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)

            background.save(filepath, "PNG", optimize=True)

        return os.path.join(self.base_path, f"{filename}.png")
