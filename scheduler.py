import time
import requests

def ping_webhooks():
    webhooks = [
        "https://user-scheduler-iy5j.onrender.com/get_free_slots",
        "https://emai-webhook-python.onrender.com/send_email",
        "https://voice-agent-zoho-webhook.onrender.com/retell"
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
        time.sleep(14 * 60)  # Sleep for 14 minutes
