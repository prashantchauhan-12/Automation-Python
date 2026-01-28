import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# REAL WORLD SCENARIO: QA & Reliability Engineering
# "We need to ensure all our 50 product pages are actually working. 
# Write a script to check them every morning."

URLS_TO_CHECK = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://this-site-does-not-exist-123.com" # Intentionally bad URL to test logic
]

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        # 200-299 is generally success
        if 200 <= response.status_code < 300:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
        return False, str(e)

def send_alert(failed_urls):
    # In a real interview, you'd configure SMTP here.
    # For this demo, we print the would-be email content.
    print("\n!!! ALERTS TRIGGERED !!!")
    print("Subject: URGENT - Website Downtime Detected")
    print(f"Time: {datetime.now()}")
    print("The following URLs are failing:")
    for url, reason in failed_urls:
         print(f" - {url} | Error: {reason}")
    print("!!! END ALERT !!!\n")

def run_monitor():
    print(f"Starting Link Checker for {len(URLS_TO_CHECK)} URLs...\n")
    failed = []
    
    for url in URLS_TO_CHECK:
        print(f"Checking {url}...", end=" ")
        is_up, status = check_status(url)
        
        if is_up:
            print(f"OK ({status})")
        else:
            print(f"FAILED ({status})")
            failed.append((url, status))
            
    if failed:
        send_alert(failed)
    else:
        print("\nAll systems operational.")

if __name__ == "__main__":
    # Requirement: pip install requests
    run_monitor()
