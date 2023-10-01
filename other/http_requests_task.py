import requests

url = 'https://dummyjson.com/products/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('error')
