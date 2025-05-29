import requests

url = 'http://localhost:8000/'

repsonse = requests.get(url)

repsonse  = repsonse.json()

print(repsonse['message'])