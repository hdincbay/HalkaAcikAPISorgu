import requests

URL = "https://placebear.com/200/300"

result = repuest.get(URL)

data = result.json()

print(data)

