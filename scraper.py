import numpy as np
import pandas as pd 
from bs4 import BeautifulSoup
import requests
from datetime import date

url='https://www.boxofficemojo.com/year/world/2021/'

def scrape_worldwide_ranking(year):
    url=f'https://www.boxofficemojo.com/daily/{year}/'#输入你要的网址
    req=requests.get(url)
    content=req.text
    soup=BeautifulSoup(content)
    rows=soup.findAll('tr')
    appended_data = []
    for index in range(1,len(rows)):
        data_row = {}
        data = rows[index].findAll('td')
        if len(data) == 0:
            continue
        data_row['Date'] = data[0].text
        data_row['Day#'] = data[2].text
        data_row['Top_10_Gross'] = data[3].text
        data_row['Releases'] = data[6].text
        appended_data.append(data_row)
    ranking_data = pd.DataFrame(appended_data, columns = ["Date","Day#","Top_10_Gross","Releases"])#修改列名
    ranking_data.to_csv(f'./yearworld_{year}.csv', index=False)# 你要储存的文件地址

todays_date = date.today()
current_year = todays_date.year
years = range(1977, current_year+1)

for year in years:
    print(year)
    scrape_worldwide_ranking(year)