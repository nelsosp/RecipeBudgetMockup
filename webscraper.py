import requests
import json

url = "https://gfsstore.com/wp-json/gfs-search/v1/get-search-results?sort=trending_popularity&store=182&dept=Produce&ctg=&posts_per_page=24&paged=1&show_score=&_=1691647379570"

headers = {
  'authority': 'gfsstore.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json; charset=UTF-8',
  'cookie': 'wordpress_google_apps_login=1f487f2b9f83c6c8564613283af67c03; wp-MyStore=MP070; wp-MyStoreID=182; MyStoreID=182; wp-cart_session=993a6ce733d3d1059b3d915b1a50686e%7C%7C1691819805%7C%7C1691819804%7C%7C6d70faa661a727ee26768034e0d6dfc3; _lr_uf_-fwixe9=e79cd410-fecd-4007-b8d1-33dc3b30f141; _gcl_au=1.1.2081797361.1691647008; _ga=GA1.1.520766485.1691647008; _mibhv=anon-1691647008194-9207402897_8112; _fbp=fb.1.1691647008239.700479037; ln_or=eyI0NTcyNzMwIjoiZCJ9; _pin_unauth=dWlkPU9HRXdZemxpTkRFdE4ySTRNUzAwWkRjMkxUZ3pNVFl0Wm1NMFltRXpORGxsWVdFNA; _lr_hb_-fwixe9%2Fgfstorecom-production={%22heartbeat%22:1691647380231}; _lr_tabs_-fwixe9%2Fgfstorecom-production={%22sessionID%22:0%2C%22recordingID%22:%225-92772342-b17a-4a5d-ae7f-61760a543d50%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691647395424}; _ga_P6EY3WNCQQ=GS1.1.1691647008.1.1.1691647396.43.0.0; MyStoreID=182; wp-MyStore=MP070; wp-MyStoreID=182',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MTY1ODkiLCJhcCI6IjExMDMxMTAwMjEiLCJpZCI6ImZhZjkzMTc1ZjYyYzhiN2MiLCJ0ciI6IjMxNGUyZDExOGY4YjI3NTI4MmNiYjhlODg1ZTM1ODAwIiwidGkiOjE2OTE2NDczOTc4NjAsInRrIjoiNjY2ODYifX0=',
  'referer': 'https://gfsstore.com/',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-314e2d118f8b275282cbb8e885e35800-faf93175f62c8b7c-01',
  'tracestate': '66686@nr=0-1-3416589-1103110021-faf93175f62c8b7c----1691647397860',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
  'x-newrelic-id': 'VwIGV1NbARABVFJaBwIHX1cE',
  'x-requested-with': 'XMLHttpRequest',
  'x-wp-nonce': '88ee5215db'
}

r = requests.request("GET", url, headers=headers)

data = json.loads(r.text)

print(data['results'])