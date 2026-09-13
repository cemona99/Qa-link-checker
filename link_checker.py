import requests
import time

def check_link(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        elapsed = round(time.time() - start_time, 2)

        if response.status_code == 200:
            print(f"✅ OK ({response.status_code}) - {url} - {elapsed}s")
        else:
            print(f"⚠️ WARNING ({response.status_code}) - {url} - {elapsed}s")
    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED - {url} - Error: {e}")

def load_urls(filename):
    with open(filename, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

if __name__ == "__main__":
    urls = load_urls("urls.txt")

    for link in urls:
        check_link(link)
