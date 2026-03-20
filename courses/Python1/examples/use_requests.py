"""Ukazka pouziti modulu requests."""

import requests

URL = "http://localhost:8080/readiness"

response = requests.get(URL, timeout=5)

data = response.json()

print(data["ready"])
