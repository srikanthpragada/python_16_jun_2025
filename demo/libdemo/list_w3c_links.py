import requests
WEBSITE = "https://www.w3schools.com"
response = requests.get(WEBSITE)
contents = response.text
#print('Contents', contents)

from bs4 import BeautifulSoup

bs = BeautifulSoup(contents, 'html.parser')

links = set()
for a in bs.find_all('a'):
    href = a['href']
    if href.startswith('javascript'):
        continue

    if not href.startswith("http"):
        href = WEBSITE  + href

    links.add(href)


for link in links:
    print(link)

print('Link Count :', len(links))
