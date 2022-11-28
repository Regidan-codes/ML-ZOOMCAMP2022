import requests
from time import sleep


url = "http://localhost:9696/predict"

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

while True:
    sleep(0.01)
    response = requests.post(url, json=client).json()
    print(response)
