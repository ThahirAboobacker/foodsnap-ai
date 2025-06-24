import requests
import bs4
from bs4 import BeautifulSoup
url="https://www.calories.info/food/fruit"
soup = requests.get(url)
soup = BeautifulSoup(soup.text, 'html.parser')

soup.prettify()
for index in range(50):
  table = soup.find( "div", {"class":"page-calories"} )
  h=table.select('tbody > tr > td > a > p')[index].get_text(strip=True)
  print(h)
