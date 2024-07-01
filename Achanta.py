import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://results.eci.gov.in/AcResultGenJune2024/ConstituencywiseS0156.htm"
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,"lxml")
#print(soup)
table = soup.find("table",class_="table table-striped table-bordered")
#print(table)
title = table.find_all("th")
#print(title)
headers = []
#print(headers)

# Extract headers
headers = [th.text.strip() for th in soup.find_all('th')]

# Extract rows
rows = []
for tr in soup.find_all('tr')[1:]:  # Skip the header row
    cells = [td.text.strip() for td in tr.find_all('td')]
    if cells:
        rows.append(cells)

# Trim headers to match row length
headers = headers[:len(rows[0])] # exact number of rows and columns

df2 = pd.DataFrame(rows,columns=headers)
#print(df2)
df2.to_csv("Achanta Stats.csv")
