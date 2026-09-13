import requests
import time

def check_link(url, report_lines):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        elapsed = round(time.time() - start_time, 2)

        if response.status_code == 200:
            result = f"OK ({response.status_code}) - {url} - {elapsed}s"
            print(f"✅ {result}")
        else:
            result = f"WARNING ({response.status_code}) - {url} - {elapsed}s"
            print(f"⚠️ {result}")
    except requests.exceptions.RequestException as e:
        result = f"FAILED - {url} - Error: {e}"
        print(f"❌ {result}")

    report_lines.append(result)

def load_urls(filename):
    with open(filename, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

def save_report(report_lines, filename="report.txt"):
    with open(filename, "w") as file:
        file.write("QA Link Check Report\n")
        file.write("=" * 40 + "\n\n")
        for line in report_lines:
            file.write(line + "\n")

if __name__ == "__main__":
    urls = load_urls("urls.txt")
    report_lines = []

    for link in urls:
        check_link(link, report_lines)

    save_report(report_lines)
    print("\n📄 Report saved to report.txt")
