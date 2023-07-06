import requests

r = requests.post('http://127.0.0.1/main')

print(r)
print(r.content)