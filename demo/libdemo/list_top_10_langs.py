import requests
WEBSITE = "https://www.tiobe.com/tiobe-index/"
response = requests.get(WEBSITE)
contents = response.text

from bs4 import BeautifulSoup
bs = BeautifulSoup(contents, 'html.parser')

table = bs.find(id = 'top20')
body = table.find('tbody')
#print(body)
rows = body.find_all("tr")

# Take only top 10 rows
for row in rows:
    cols = row.find_all("td")
    print(f"{cols[4].text:20}  {cols[5].text:5}")

