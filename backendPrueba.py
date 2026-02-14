import requests

url = "http://127.0.0.1:8000/logs"

headers = {
    "Authorization": "Bearer abc123-super-token"
}

payload = {
    "level": "INFO",
    "message": "email enviado",
    "extra": {
        "user": "test@gmail.com",
        "latency": 213
    }
}

r = requests.post(url, json=payload, headers=headers)

print(r.status_code, r.text)
