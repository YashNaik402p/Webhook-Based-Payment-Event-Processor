import requests
import time
num=1
for i in range(6):
    requests.post("http://localhost:5000/webhook", json={
        "event": "payment_success",
        "user_id": num
    })
    num+=1
    time.sleep(4)
    