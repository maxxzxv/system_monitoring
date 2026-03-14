import psutil
import requests
import time

API_URL = "http://127.0.0.1:8000/metrics"
INTERVAL = 5

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }

def send_metrics(metrics):
    try:
        response = requests.post(API_URL, json=metrics)
        print("Sent: ", metrics, "Response: ", response.json())
    except Exception as e:
        print("Error sending metrics: ", e)

def main():
    while True:
        metrics = collect_metrics()
        send_metrics(metrics)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()