import requests
from bs4 import BeautifulSoup

URL = "https://chamonix.com.au/consulting-service/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.find("main"))

body = soup.find("main").find_all(["h1","h2","h3", "p"])

for p in body:
    print(p.text.strip())