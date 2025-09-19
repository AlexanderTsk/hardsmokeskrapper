import re
from playwright.async_api import async_playwright, Page
from entity.parsed_product import ParsedProduct


class PlaywrightBrowser:
    def __init__(self, url: str, name_regex: str | None = None):
        self.url = url
        self.name_regex = name_regex

    async def parse(self) -> list[ParsedProduct]:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(self.url)

            await self._unpack_products(page)
            product_links = await self._get_product_links(page)
            print(f"Products found: {len(product_links)}")
            
            parsed_products = []
            for link in product_links:
                parsed_product = await self._parse_product(link, page)

                if self.name_regex and not re.search(self.name_regex, parsed_product.name, re.IGNORECASE):
                    continue  

                parsed_products.append(parsed_product)

            await browser.close()
        return parsed_products

    async def _unpack_products(self, page: Page):
        show_more_btn = page.locator('.seomore_a')

        while await show_more_btn.count() > 0:
            try:
                await show_more_btn.click()
                await page.wait_for_timeout(2000) 
            except Exception:
                break 

    async def _get_product_links(self, page: Page) -> list[str]:
        product_links = await page.locator(
            ".cat_prod .product-layout .product-block .product-details .product-name a.sales-name-text"
        ).evaluate_all("els => els.map(el => el.href)")
        return product_links

    async def _parse_product(self, url: str, page: Page) -> ParsedProduct:
        await page.goto(url)

        title = (await page.locator('h1').text_content()) or ""
     
        attributes: dict[str, str] = {}
        attribute_elements = await page.locator('.product-attribute-card').all()

        for attr in attribute_elements:
            attr_name = (await attr.locator('.product-attribute-name').text_content()) or ""
            attr_value = (await attr.locator('.product-attribute-value').text_content()) or ""

            clean_name = attr_name.strip().rstrip(":")
            attributes[clean_name] = attr_value.strip()

        description = (await page.locator('.product-description-text').nth(0).inner_html()) or ""

        image = (await page.locator('div.image a.thumbnail').nth(0).get_attribute('href')) or ""

        gallery = []
        gallery_carousel = page.locator('#additional-carousel').first
        gallery_elements = await gallery_carousel.locator('.swiper-slide .product-block a').all()
        for gallery_image in gallery_elements:
            image_src = await gallery_image.get_attribute('href')
            if image_src:
                gallery.append(image_src)

        return ParsedProduct(
            name=title.strip(),
            attributes=attributes,
            description=description.strip(),
            image=image,
            gallery=gallery
        )
