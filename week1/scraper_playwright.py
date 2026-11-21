from playwright.sync_api import sync_playwright

def fetch_website_contents(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded")

            title = page.title() or "No title found"

            text = page.locator("body").inner_text()

            return (title + "\n\n" + text)[:2000]

        finally:
            browser.close()