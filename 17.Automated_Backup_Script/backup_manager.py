import os
import shutil
import time
from datetime import datetime, timedelta

# REAL WORLD SCENARIO: IT Operations / SysAdmin
# "Automate the backup of our 'Important_Docs' folder every day at 5 PM.
#  Also, auto-delete backups older than 7 days to save disk space."

SOURCE_FOLDER = "My_Critical_Data"
BACKUP_FOLDER = "Backups"
RETENTION_DAYS = 7

def create_dummy_data():
    if not os.path.exists(SOURCE_FOLDER):
        os.makedirs(SOURCE_FOLDER)
        with open(os.path.join(SOURCE_FOLDER, "secret_plans.txt"), "w") as f:
            f.write("Project X Launch Code: 12345")
        print(f"Created dummy folder '{SOURCE_FOLDER}' to back up.")

def perform_backup():
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)
        
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}")
    
    # Creates backup_2024-01-28_10-00-00.zip
    shutil.make_archive(archive_name, 'zip', SOURCE_FOLDER)
    print(f"Backup created: {archive_name}.zip")

def rotate_backups():
    print("\nChecking for old backups to delete...")
    now = time.time()
    cutoff = now - (RETENTION_DAYS * 86400) # 86400 seconds in a day
    
    for filename in os.listdir(BACKUP_FOLDER):
        file_path = os.path.join(BACKUP_FOLDER, filename)
        
        if os.path.isfile(file_path) and filename.endswith(".zip"):
            file_mod_time = os.path.getmtime(file_path)
            
            if file_mod_time < cutoff:
                os.remove(file_path)
                print(f"Deleted old backup: {filename}")
            else:
                # Calculate days remaining (just for demo info)
                age = (now - file_mod_time) / 86400
                print(f"Kept {filename} (Age: {age:.2f} days)")

if __name__ == "__main__":
    # 1. Setup
    create_dummy_data()
    
    # 2. Run Backup
    perform_backup()
    
    # 3. Cleanup Old Files
    rotate_backups()
