import requests
import json
import pandas as pd
import time


url = "https://foodcombo.com/api/recipes/tag-alfredo?returns=recipes&visible=30&page=1&offset=-2"

headers = {
    'authority': 'foodcombo.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__utmz=62383291.1691776895.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.1.109090082.1691776895; PHPSESSID=bokeo8hqhkgunrs04vc8hc28k1; __utma=62383291.1443524468.1691776895.1691776895.1691885430.2; __utmc=62383291; __utmt=1; _ga_ZF4D68G8KK=GS1.1.1691885429.2.1.1691885596.60.0.0; __utmb=62383291.7.9.1691885602475',
    'referer': 'https://foodcombo.com/find-recipes-by-ingredients/tag-alfredo',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'x-requested-with': 'XMLHttpRequest'
}


# r = requests.request("GET", url, headers=headers)

# data = json.loads(r.text)


# print(data['recipes'])


data_list = []


for page in range(0, 12):
    url = f"https://foodcombo.com/api/recipes/tag-alfredo?returns=recipes&visible=30&page={page}&offset=-2"
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    data_list.extend(data['recipes'])
    time.sleep(3)
    print(f'Getting page {page}', 'waiting..')

products = pd.json_normalize(data_list)
products.to_csv('recipe1.csv')


# 0-12
