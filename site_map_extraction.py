import requests
import xml.etree.ElementTree as ET
import logging

def map_sitemap(sitemap_index):
    sitemap_urls = []
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(sitemap_index,headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        root = ET.fromstring(response.content)
        
        # single sitemap without index case, found in SIG site
        if root.tag.endswith("urlset"):
            sitemap_urls.append(sitemap_index)
            return sitemap_urls
        
        for sitemap in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
            loc = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
            if loc is not None:
                sitemap_urls.append(loc.text)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
    except ET.ParseError as e:
        logging.error(f"XML parsing error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return sitemap_urls

def map_urls(sitemap_xmls):
  urls = {}
  for sitemap in sitemap_xmls:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(sitemap,headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        sitemap_xml = ET.fromstring(response.content)

        # Extract the loc tags, which contain the URLs
        key = sitemap.split('/')[-1].split('.')[0]
        value = []
        for url in sitemap_xml.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
            loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
            if loc is not None:
                value.append(loc.text)
        urls[key] = value
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
    except ET.ParseError as e:
        logging.error(f"XML parsing error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
          
  return urls

def map(sitemap_index):
    sitemap_xmls = map_sitemap(sitemap_index)
    urls = map_urls(sitemap_xmls)
    return urls

def test():
    urls = map("https://www.sig.com/sitemap.xml")
    for key, value in urls.items():
        print((key, value))
        print(len(value))
        