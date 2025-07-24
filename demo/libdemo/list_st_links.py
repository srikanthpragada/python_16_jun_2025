import requests

WEBSITE = "https://www.srikanthtechnologies.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(WEBSITE, headers=headers)
contents = response.text

from bs4 import BeautifulSoup

bs = BeautifulSoup(contents, 'html.parser')

links = set()
for a in bs.find_all('a'):
    href = a['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        href = WEBSITE + "/" + href

    links.add(href)

for link in links:
    print(link)
