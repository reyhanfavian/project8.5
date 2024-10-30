import requests

api_key = 'f01ad9d6-b2c7-4799-83bc-3ec2373ff790'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)