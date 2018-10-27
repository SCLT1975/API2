import requests
import json

CMC_PRO_API_KEY = '902988e2-150c-4bc6-97d6-b79f9f69d14a'

headers = {'X-CMC_PRO_API_KEY': '8eafcad5-5784-4e01-86e9-26bb819e3c62'}
limit = 10
sort = 'market cap'
payload = {'limit': '10', 'sort_dir': 'desc', 'sort': 'volume_24h'}


r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', headers=headers, params=payload)

r.json()

print (r.json())