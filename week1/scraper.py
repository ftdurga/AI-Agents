from bs4 import BeautifulSoup
import requests

# requests allows Python to send HTTP requests to websites.
# requests retrieves the website.
# BeautifulSoup parses and extracts information from it.

# Standard headers to fetch a website
# When Python sends a request to a website, it can identify itself through HTTP headers.
# The User-Agent tells the website what kind of client is making the request.
# In this case, we're making Python identify itself as something resembling a Chrome browser running on Windows.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    
    # soup as a Python-accessible representation of the website's HTML structure
    soup = BeautifulSoup(response.content, "html.parser")
    
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            # Recursively destroys this PageElement and its children.
            irrelevant.decompose()
        
        # Get all child strings of this PageElement, concatenated using the given separator
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    # Limit the output to 2,000 characters.
    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url):
    """
    Return the links on the webiste at the given url
    I realize this is inefficient as we're parsing twice! This is to keep the code in the lab simple.
    Feel free to use a class and optimize it!
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
