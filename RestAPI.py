import requests
import json
country = "afghanistan"
response = requests.get('https://jsonmock.hackerrank.com/api/countries?name={}'.format(country))
print(response.json()['data'][0]['capital'])