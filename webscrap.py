import requests
from bs4 import BeautifulSoup

url = "https://www.calories.info/food/fruit"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main data container
table = soup.find("div", {"class": "page-calories"})

# Go through each row of the table
rows = table.select('tbody > tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:
        # Extract fruit name from <a> inside the first column
        fruit = cols[0].text
        weight = cols[1].text
        calories = cols[2].text
