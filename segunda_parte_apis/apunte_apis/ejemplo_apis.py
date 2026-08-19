# import requests
# import json
# BASE_URL = 'https://fakestoreapi.com'

# response = requests.get(f"{BASE_URL}/products")

# leido = response.json()

# for i in leido:
#     print(i['image'])
#     print("----")
#     print("----")
#     print("----")


import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())
print(response.url)