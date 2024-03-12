import requests
import xml.etree.ElementTree as ET

def map_sitemap(sitemap_index):
    sitemap_urls = []
    try:
        response = requests.get(sitemap_index)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        sitemap_index_xml = ET.fromstring(response.content)
        
        for sitemap in sitemap_index_xml.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
            loc = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
            if loc is not None:
                sitemap_urls.append(loc.text)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return sitemap_urls

def map_urls(sitemap_xmls):
  urls = {}
  for sitemap in sitemap_xmls:
    try:
        response = requests.get(sitemap)
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
        print(f"Request error: {e}")
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
          
  return urls

def map(sitemap_index):
    sitemap_xmls = map_sitemap(sitemap_index)
    urls = map_urls(sitemap_xmls)
    return urls

def test():
    urls = map("https://chamonix.com.au/sitemap.xml")
    for key, value in urls.items():
        print((key, value))
        print(len(value))