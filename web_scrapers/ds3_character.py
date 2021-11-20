import json
import requests
from bs4 import BeautifulSoup

# get data
data = requests.get('https://darksouls.fandom.com/wiki/Category:Dark_Souls_III:_Characters')

# load data into bs4
soup = BeautifulSoup(data.text, features="html5lib")
data_obj = soup.find_all('a', { 'class' : 'category-page__member-link' })

data_dict = {}
for i in range(len(data_obj)):
    data_dict[data_obj[i].text] = "https://darksouls.fandom.com"+data_obj[i].get('href')

# Serializing json
json_object = json.dumps(data_dict, indent=2)

# Writing to sample.json
with open("./data/ds3_characters.json", "w") as outfile:
    outfile.write(json_object)
