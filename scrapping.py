from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

website_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(website_url)
print(page)

soup=bs(page.text,'html.parser')
stars_table=soup.find('table')
temp_list=[]
table_rows=stars_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td] #rstrip() deletes the extra blank spaces
    temp_list.append(row)

name=[]
distance=[]
mass=[]
radius=[]
luminosity=[]

#As we have to take data from different columns, we will have to mention its location
for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])

#Creating a dataFrame and then converting it to a csv file
df=pd.DataFrame(list(zip(name,distance,mass,radius,luminosity)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)
df.to_csv('brightest_stars.csv')