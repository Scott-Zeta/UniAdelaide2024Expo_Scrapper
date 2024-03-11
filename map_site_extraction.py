import requests
import xml.etree.ElementTree as ET

def map(sitemap_url):
  urls = []
  try:
    # Fetch the sitemap
    response = requests.get(sitemap_url)
    # Parse the XML content of the sitemap
    sitemap_xml = ET.fromstring(response.content)

    # Extract the loc tags, which contain the URLs
    for url in sitemap_xml.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc is not None:
            urls.append(loc.text)
  except requests.exceptions.RequestException as e:
      print(f"Request error: {e}")
  except ET.ParseError as e:
      print(f"XML parsing error: {e}")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
          

  print(urls)
  # Now, urls contains all the URLs found in the sitemap
  return url

map("https://chamonix.com.au/page-sitemap1.xml")