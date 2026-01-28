import re
import csv
from collections import Counter

# INTERVIEW QUESTION: "Parse this messy access log and tell me the top 5 IPs visiting our site."
# Strategy: Regular Expressions (Regex)
# Regex is a SUPERPOWER in automation. If you know regex, you can parse anything.

LOG_FILE = "server_access.log"

def create_dummy_log():
    # Simulating standard Apache/Nginx logs
    logs = [
        '192.168.1.1 - - [28/Jan/2026:10:00:01] "GET /home HTTP/1.1" 200 1024',
        '192.168.1.2 - - [28/Jan/2026:10:00:02] "POST /login HTTP/1.1" 403 512',
        '10.0.0.5 - - [28/Jan/2026:10:00:03] "GET /dashboard HTTP/1.1" 200 2048',
        '192.168.1.1 - - [28/Jan/2026:10:00:04] "GET /images/logo.png HTTP/1.1" 200 4096',
        '172.16.0.1 - - [28/Jan/2026:10:00:05] "GET /about HTTP/1.1" 404 102',
        '192.168.1.1 - - [28/Jan/2026:10:00:06] "POST /settings HTTP/1.1" 200 512',
        '10.0.0.5 - - [28/Jan/2026:10:00:07] "GET /contact HTTP/1.1" 200 1024'
    ]
    # Replicate to make it bigger
    with open(LOG_FILE, "w") as f:
        for _ in range(20): # 140 lines total
            for line in logs:
                f.write(line + "\n")
    print(f"Generated {LOG_FILE}")

def parse_logs():
    print("Analyzing Logs...")
    
    # Regex Pattern Breakdown:
    # (\d+\.\d+\.\d+\.\d+)  -> Match Group 1: IP Address (digits.digits...)
    # .*?                   -> Non-greedy match for anything in between
    # "(\w+)                -> Match Group 2: The HTTP Method (GET/POST)
    # \s                    -> Space
    # (/[^"]*)              -> Match Group 3: The Endpoint (starts with /)
    # .*?                   -> Rest of the line
    # (\d{3})               -> Match Group 4: Status Code (3 digits)
    
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?"(\w+)\s(/[^"]*).*?(\d{3})')
    
    ip_counter = Counter()
    status_counter = Counter()
    endpoints = []

    with open(LOG_FILE, "r") as f:
        for line in f:
            match = log_pattern.search(line)
            if match:
                ip_addr = match.group(1)
                method = match.group(2)
                path = match.group(3)
                status = match.group(4)
                
                ip_counter[ip_addr] += 1
                status_counter[status] += 1
                endpoints.append(path)

    # Reporting
    print("\n--- TOP VISITOR IPs ---")
    for ip, count in ip_counter.most_common(3):
        print(f"{ip}: {count} requests")

    print("\n--- STATUS CODE DISTRIBUTION ---")
    for code, count in status_counter.items():
        print(f"HTTP {code}: {count} times")
        
    print("\n--- ENDPOINTS ---")
    print(f"Total endpoints accessed: {len(endpoints)}")

if __name__ == "__main__":
    create_dummy_log()
    parse_logs()
