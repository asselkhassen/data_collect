import requests
import json

username = 'asselkhassen'
response = requests.get(f'https://api.github.com/users/{username}/repos')

j_data = response.json()

with open('task-1.json', 'w') as f:
    json.dump(j_data, f)

for el in j_data:
    print(el['name'])
