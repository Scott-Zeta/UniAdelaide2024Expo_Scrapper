import requests
import xml.etree.ElementTree as ET

# Replace this with the sitemap URL
sitemap_url = "https://chamonix.com.au/page-sitemap1.xml"

# Fetch the sitemap
response = requests.get(sitemap_url)
# Parse the XML content of the sitemap
sitemap_xml = ET.fromstring(response.content)
# print(sitemap_xml)
urls = []

# Extract the loc tags, which contain the URLs
for url in sitemap_xml.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
    loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    if loc is not None:
        urls.append(loc.text)

print(urls)
# Now, urls contains all the URLs found in the sitemap
