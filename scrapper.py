import requests
from bs4 import BeautifulSoup
import logging
import time

def scrape(url):
    try:
        # This is to avoid being blocked by the Optiver 429 too many requests
        # Can be implemented as a backoff strategy if needed
        # time.sleep(0.1) 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        page = requests.get(url,headers=headers)
        page.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(page.content, "html.parser")
        
        # clean the elements not needed
        for unwanted_section in soup.select('header, footer, nav, .sidebar, div.menu_nav'):
            # div.menu_nav As the Fultonhogan use div to build everything, include a horrible collapsible menu can take the entire page
            unwanted_section.decompose()
        # print(soup.prettify())
        main_content = soup.find("main")
        if main_content is None:
            logging.warning(f"No <main> element found. For {url}")
            body = []
            if soup.find("div",class_="text"):
                # This only appeared in citadelsecurities site, with no main element, content is inside div
                body = soup.find("div",class_="text").find_all(["h1", "h2", "h3", "p","li","div","table"])
            elif soup.find("div",role="main"):
                # This only appeared in Flinders Port Holdings, they don't use the footer elements,
                # and have an addtional mobile menu at the bottom, but not mark as nav or header
                body = soup.find("div",role="main").find_all(["h1", "h2", "h3", "p","li","table"])
            elif soup.find("div",class_="main"):
                # This is only for GPAEngneering, I would say they are much better than others
                body = soup.find("div",class_="main").find_all(["h1", "h2", "h3", "p","li","table"])
            else:
                # Common case
                body = soup.find_all(["h1", "h2", "h3", "p","li","table"])
            return body

        body = main_content.find_all(["h1", "h2", "h3", "p","li","table"])

        return body

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def test():
    url = "https://tbhconsultancy.com/experience/airport-link-northern-busway/"
    body = scrape(url)
    for tag in body:
        print(tag.text.strip())
        