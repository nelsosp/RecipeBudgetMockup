import requests
import json
import pandas as pd
import time

url = "https://gfsstore.com/wp-json/gfs-search/v1/get-search-results?sort=trending_popularity&store=182&dept=Meat%2B%2526%2BSeafood&ctg=&posts_per_page=24&paged=2&show_score=&_=1691725151051"

headers = {
    'authority': 'gfsstore.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    'cookie': 'wp-MyStore=MP070; wp-MyStoreID=182; MyStoreID=182; wp-cart_session=993a6ce733d3d1059b3d915b1a50686e%7C%7C1691819805%7C%7C1691819804%7C%7C6d70faa661a727ee26768034e0d6dfc3; _gcl_au=1.1.2081797361.1691647008; _ga=GA1.1.520766485.1691647008; _mibhv=anon-1691647008194-9207402897_8112; _fbp=fb.1.1691647008239.700479037; ln_or=eyI0NTcyNzMwIjoiZCJ9; _pin_unauth=dWlkPU9HRXdZemxpTkRFdE4ySTRNUzAwWkRjMkxUZ3pNVFl0Wm1NMFltRXpORGxsWVdFNA; wordpress_google_apps_login=2c5d8b2769c9dfa8dedde96a32081d87; _lr_uf_-fwixe9=b8fe769e-2772-4b81-b153-60b364363619; _lr_hb_-fwixe9%2Fgfstorecom-production={%22heartbeat%22:1691725151299}; _ga_P6EY3WNCQQ=GS1.1.1691725134.5.1.1691725162.32.0.0; _lr_tabs_-fwixe9%2Fgfstorecom-production={%22sessionID%22:0%2C%22recordingID%22:%225-cb0d0ee0-9c82-46df-844b-01d7b5f62592%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691725266848}; MyStoreID=182; wp-MyStore=MP070; wp-MyStoreID=182',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MTY1ODkiLCJhcCI6IjExMDMxMTAwMjEiLCJpZCI6IjE5MDFjYjE4MTZiZTdlYjMiLCJ0ciI6ImEzODNlYjY0MGY2ZmZlMmJkOWQxNjcyM2ZkYTM0MjAwIiwidGkiOjE2OTE3MjUyNjg5MDIsInRrIjoiNjY2ODYifX0=',
    'referer': 'https://gfsstore.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-a383eb640f6ffe2bd9d16723fda34200-1901cb1816be7eb3-01',
    'tracestate': '66686@nr=0-1-3416589-1103110021-1901cb1816be7eb3----1691725268902',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
    'x-newrelic-id': 'VwIGV1NbARABVFJaBwIHX1cE',
    'x-requested-with': 'XMLHttpRequest',
    'x-wp-nonce': '404df977da'
}

# r = requests.request("GET", url, headers=headers)

# data = json.loads(r.text)

data_list = []


for page in range(1, 18):
    url = f"https://gfsstore.com/wp-json/gfs-search/v1/get-search-results?sort=trending_popularity&store=182&dept=Meat%2B%2526%2BSeafood&ctg=&posts_per_page=24&paged={page}&show_score=&_=1691725151051"
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    data_list.extend(data['results']['search_results'])
    time.sleep(3)
    print(f'Getting page {page}', 'waiting..')

products = pd.json_normalize(data_list)
products.to_csv('ingredientmeats_price1.csv')
