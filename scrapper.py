import requests
from bs4 import BeautifulSoup
import logging

def scrape(url):
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raises an HTTPError for bad responses

        soup = BeautifulSoup(page.content, "html.parser")

        main_content = soup.find("main")
        if main_content is None:
            logging.warning(f"No <main> element found. For {url}")
            body = soup.find_all(["h1", "h2", "h3", "p","li"])
            return body

        body = main_content.find_all(["h1", "h2", "h3", "p","li"])

        return body

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

# scrape("https://chamonix.com.au/consulting-service/")