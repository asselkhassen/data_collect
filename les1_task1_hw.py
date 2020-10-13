import requests
import json

username = 'asselkhassen'
response = requests.get(f'https://api.github.com/users/{username}/repos')

j_data = response.json()
my_repos = []
for el in j_data:
    my_repos.append(el['name'])

with open('task-1.json', 'w') as f:
    json.dump(my_repos, f)

for el in j_data:
    print(el['name'])


