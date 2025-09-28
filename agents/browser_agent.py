
from playwright.sync_api import sync_playwright

def scrape_url_to_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        text = page.content()
        browser.close()
        return text
