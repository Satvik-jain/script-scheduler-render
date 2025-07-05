import time
import requests

def ping_webhooks():
    webhooks = [
        "https://api.render.com/deploy/srv-d1knitqdbo4c73a31dt0?key=WaW3SXFCkJo"
    ]
    
    for url in webhooks:
        try:
            response = requests.get(url, timeout=10)
            print(f"Pinged {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to reach {url}: {e}")

if __name__ == "__main__":
    while True:
        ping_webhooks()
        time.sleep(10* 60)  # Sleep for 14 minutes
