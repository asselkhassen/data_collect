import requests
import json

authentication_api = 'http://ecargo.sapasoft.kz/api/authenticate'
moderation_api = 'http://ecargo.sapasoft.kz/api/companies-filter'

auth_params = {'username': '+7(777)777-7777', 'password': 'admin', 'sms': False, 'web': True}
headers={'Content-type':'application/json', 'Accept':'application/json'}

response = requests.post(authentication_api, json=auth_params, headers=headers)
token = 'Bearer ' + response.json()['id_token']

headers.update({'Authorization': token})
companies = requests.post(moderation_api, params={'page': 0, 'size': 20}, json={}, headers=headers)

with open('task-2.json', 'w') as f:
    json.dump(companies.json(), f)