
from bs4 import BeautifulSoup
import requests

url = 'http://www.agriculture.gov.au/pests-diseases-weeds/plant#indentify-pests-diseases'
data = requests.get(url)

soup = BeautifulSoup(data.content, 'lxml')
main_div = soup.find(class_="flex-container")

plant_dieses = []
plant_dieses_urls = []
plant_dieses_image_urls = []
main_url = 'http://www.agriculture.gov.au'
for i in main_div:
    dieses_sub_url = i.find('a').get('href')
    dieses_image_url = i.find('img').get('src')
    dieses_name = i.find('a').text.strip()
    plant_dieses.append(dieses_name)
    plant_dieses_urls.append(str(main_url)+str(dieses_sub_url))
    plant_dieses_image_urls.append(str(main_url)+str(dieses_image_url))

total = []
for l ,m ,n in zip(plant_dieses_urls, plant_dieses_image_urls, plant_dieses):
    try:
        url = l
        data = requests.get(url)
        soup=BeautifulSoup(data.content , 'lxml')
        main_tag = soup.find(class_="pest-header-content")
        d = {}
        for i in main_tag:
            a = i.findAll('strong')
            for j in a:
                if len(j.text)>1:
                    d[j.text.strip()] = j.next_sibling.strip()
                    d['plant_dieses_url'] = l
                    d['plant_dieses_image_url'] = m
                    d['plant_dieses_name'] = n
        total.append(d)
    except Exception as e:
        d = {}
        d['plant_dieses_url'] = l
        d['plant_dieses_image_url'] = m
        d['plant_dieses_name'] = n
        d['other_factor'] = 'Not Found'
        total.append(d)

# Saving data to csv file
import pandas as pd

df = pd.DataFrame(total)
df.drop(['At','other_factor','risk:'],axis=1,inplace=True)
df.fillna('Not Found')
df.to_csv('plant_dieses.csv')

# Downloading Images
import urllib.request
for img_url in plant_dieses_image_urls:
    dieses = img_url.split('http://www.agriculture.gov.au/SiteCollectionImages/pests-diseases-weeds/')[1]
    urllib.request.urlretrieve(img_url, f"Dieses_Images/{dieses}.jpg")