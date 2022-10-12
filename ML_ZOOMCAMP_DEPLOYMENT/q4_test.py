import requests
import json

url = "http://localhost:9696/predict"
customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=customer)
result = response.json()

print(result)