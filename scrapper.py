import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raises an HTTPError for bad responses

        soup = BeautifulSoup(page.content, "html.parser")

        main_content = soup.find("main")
        if main_content is None:
            print(f"No <main> element found. For {url}")
            body = soup.find_all(["h1", "h2", "h3", "p","li"])
            return body

        body = main_content.find_all(["h1", "h2", "h3", "p","li"])
        
        # for tag in body:
        #     print(tag.text.strip())

        return body

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# scrape("https://chamonix.com.au/consulting-service/")