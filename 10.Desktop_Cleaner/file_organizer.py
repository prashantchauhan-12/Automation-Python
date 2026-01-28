import os
import shutil

# STRATEGY: File System Management
# This demonstrates manipulating files directly: Moving, Renaming, Creating Directories.
# This is a classic "Sysadmin" automation task.

def create_dummy_files(base_dir):
    """Creates a messy folder with random files to demonstrate cleaning."""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Dictionary of filename: content
    files = {
        'photo.jpg': 'image data',
        'document.pdf': 'pdf data',
        'notes.txt': 'text data',
        'installer.exe': 'binary data',
        'archive.zip': 'compressed data',
        'song.mp3': 'audio data',
        'random_script.py': 'print("hello")'
    }
    
    for name, content in files.items():
        with open(os.path.join(base_dir, name), 'w') as f:
            f.write(content)
    print(f"Created dummy files in '{base_dir}'")

def organize_directory(target_dir):
    print(f"Organizing directory: {target_dir}...")
    
    # Category Rules
    EXTENSIONS = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Docs': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Software': ['.exe', '.msi', '.py', '.js'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar']
    }
    
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # Skip directories, only organize files
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            moved = False
            for category, exts in EXTENSIONS.items():
                if file_ext in exts:
                    # Create category folder if not exists
                    cat_dir = os.path.join(target_dir, category)
                    os.makedirs(cat_dir, exist_ok=True)
                    
                    # Move file
                    shutil.move(file_path, os.path.join(cat_dir, filename))
                    print(f"Moved {filename} -> {category}/")
                    moved = True
                    break
            
            # If no extension matched, move to Others
            if not moved:
                other_dir = os.path.join(target_dir, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, filename))
                print(f"Moved {filename} -> Others/")

if __name__ == "__main__":
    # 1. Setup a Test Folder so we don't mess up your actual computer
    TEST_DIR = "Test_Junk_Folder"
    create_dummy_files(TEST_DIR)
    
    print("\nCheck the folder 'Test_Junk_Folder'. It is currently messy.")
    input("Press Enter to run the cleanup automation...")
    
    # 2. Run Automation
    organize_directory(TEST_DIR)
    print("\nCleanup Complete! Check 'Test_Junk_Folder' again.")
