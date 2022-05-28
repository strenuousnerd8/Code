import requests
import json
country = input().capitalize()
response = requests.get('https://jsonmock.hackerrank.com/api/countries?name={}'.format(country))
if response.json()['data'] != []:
    print(response.json()['data'][0]['capital'])
else: print(-1)