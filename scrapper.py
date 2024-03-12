import requests
from bs4 import BeautifulSoup
import logging

def scrape(url):
    try:
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
                body = soup.find("div",class_="text").find_all(["h1", "h2", "h3", "p","li","div"])
            elif soup.find("div",role="main"):
                # This only appeared in Flinders Port Holdings, they don't use the footer elements,
                # and have an addtional mobile menu at the bottom, but not mark as nav or header
                body = soup.find("div",role="main").find_all(["h1", "h2", "h3", "p","li"])
            elif soup.find("div",class_="main"):
                # This is only for GPAEngneering, I would say they are much better than others
                body = soup.find("div",class_="main").find_all(["h1", "h2", "h3", "p","li"])
            else:
                # Common case
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

def test():
    url = "https://www.flindersportholdings.com.au/graduate-program/"
    body = scrape(url)
    for tag in body:
        print(tag.text.strip())

# test()