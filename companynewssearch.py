import requests


url = 'https://v3-api.newscatcherapi.com/api/search?'

params = {'q': ORG_entity_name=Apple OR "Apple Inc"}

headers = {'x-api-token': 'your_key_1'}

response = requests.get(url, params=params, headers=headers)




