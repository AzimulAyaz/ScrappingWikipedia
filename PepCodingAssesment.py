import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/A"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
paras = soup.find_all('li')
paras2 = soup.find_all('ul')
print(soup.find_all("li", class_="toclevel-1 tocsection-1"))
print(soup.find_all("li", class_="toclevel-2 tocsection-2"))
print(soup.find_all("li", class_="toclevel-1 tocsection-3"))

print(soup.find_all("li", class_="toclevel-2 tocsection-4"))
print(soup.find_all("li", class_="toclevel-2 tocsection-5"))
print(soup.find_all("li", class_="toclevel-2 tocsection-6"))
