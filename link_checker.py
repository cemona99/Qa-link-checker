import requests

def check_link(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ OK ({response.status_code}) - {url}")
        else:
            print(f"⚠️ WARNING ({response.status_code}) - {url}")
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
