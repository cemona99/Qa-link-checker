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

if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://thisurldoesnotexist12345.com"
    ]

    for link in urls:
        check_link(link)
