!pip install openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["Fruits","Weight","Calories"])
for row in rows:
  cols = row.find_all('td')
  if len(cols) >= 3:
        # Extract fruit name from <a> inside the first column
        fruit = cols[0].text
        weight = cols[1].text
        calories = cols[2].text
        ws.append([fruit,weight,calories])
wb.save("calories.xlsx")

