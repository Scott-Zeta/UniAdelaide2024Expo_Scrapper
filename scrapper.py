import requests
from bs4 import BeautifulSoup

def scrap(url):
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raises an HTTPError for bad responses

        soup = BeautifulSoup(page.content, "html.parser")

        main_content = soup.find("main")
        if main_content is None:
            print("No <main> element found.")
            return []

        body = main_content.find_all(["h1", "h2", "h3", "p"])
        
        for tag in body:
            print(tag.text.strip())

        return body

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

scrap("https://chamonix.com.au/consulting-service/")