import time
import requests

while True:
    print(requests.get("http://localhost:8080/productpage?u=normal"))
    time.sleep(2)