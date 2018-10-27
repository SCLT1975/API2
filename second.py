import requests
import time
import numpy


CMC_PRO_API_KEY = '902988e2-150c-4bc6-97d6-b79f9f69d14a'

headers = {'X-CMC_PRO_API_KEY': '8eafcad5-5784-4e01-86e9-26bb819e3c62'}
limit = 10
sort = 'market cap'
payload = {'limit': '10', 'sort_dir': 'desc', 'sort': 'volume_24h'}
start_time = time.time()
request_time_start = []
request_time_finish = []

i = 0
while i < 8:
    i = i + 1
    specific_request_start = time.time()
    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', headers=headers,
                     params=payload)
    specific_request_finish = time.time()
    request_time_start.append(specific_request_start)
    request_time_finish.append(specific_request_finish)

time_of_request = []

n_start = numpy.array(request_time_start, float)
n_finish = numpy.array(request_time_finish, float)

RPS_array = n_finish - n_start

latency_for_80 = numpy.percentile(RPS_array, 80)


print (RPS_array)
print(latency_for_80)