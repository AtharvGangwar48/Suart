from playwright.async_api import async_playwright

class PlaywrightScraper:
    async def scrape_page(self, url: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            
            content = await page.content()
            await browser.close()
            
            return content