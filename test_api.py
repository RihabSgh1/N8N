import requests

# URL de base de l'API
base_url = "http://127.0.0.1:8000"

# Test GET /
response_get = requests.get(f"{base_url}/")
print("GET / response status:", response_get.status_code)
print("GET / response body:", response_get.json())

# Test POST /postdata
payload = {"key": "value"}
response_post = requests.post(f"{base_url}/postdata", json=payload)
print("POST /postdata response status:", response_post.status_code)
print("POST /postdata response body:", response_post.json())
