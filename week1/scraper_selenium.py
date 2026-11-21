from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def fetch_website_contents(url):

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        title = driver.title or "No title found"

        # Extract visible text from the website body
        text = driver.find_element(By.TAG_NAME, "body").text

        return (title + "\n\n" + text)[:2000]

    finally:
        driver.quit()

def fetch_website_links(url):

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        elements = driver.find_elements(By.TAG_NAME, "a")

        links = [
            element.get_attribute("href")
            for element in elements
        ]

        return [link for link in links if link]

    finally:
        driver.quit()