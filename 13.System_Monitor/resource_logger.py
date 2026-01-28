import psutil
import time
import csv
from datetime import datetime

# STRATEGY: System Monitoring & Logging
# "Write a script that logs CPU usage every 5 seconds so we can debug a server crash."
# Concepts: System libraries (psutil), Persistent Logging (CSV/Append mode), Timestamps.

LOG_FILE = "system_stats.csv"

def log_system_stats(duration_seconds=20):
    print(f"Monitoring System Resources for {duration_seconds} seconds...")
    
    # Open CSV in Append mode ('a') so we don't overwrite past logs
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header if file is empty
        if f.tell() == 0:
            writer.writerow(["Timestamp", "CPU_Usage_%", "RAM_Usage_%", "Disk_Usage_%"])
            
        start_time = time.time()
        
        while (time.time() - start_time) < duration_seconds:
            # 1. Gather Data
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = psutil.cpu_percent(interval=1) # Blocking call for 1 sec
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            
            # 2. Write to File
            row = [timestamp, cpu, ram, disk]
            writer.writerow(row)
            
            print(f"Logged: {row}")
            # interval=1 acts as our sleep, so no extra sleep needed
            
    print(f"\nMonitoring complete. Data saved to {LOG_FILE}")

if __name__ == "__main__":
    # Requirement: pip install psutil
    log_system_stats()
