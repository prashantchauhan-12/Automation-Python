import pyautogui
import time
import os

# INTERVIEW QUESTION: "How do you automate a legacy desktop application that has no API?"
# Answer: "I would use a GUI automation tool like PyAutoGUI to simulate mouse clicks and keystrokes."
# WARNING: This script takes control of your mouse. Move your mouse to a corner to abort (FailSafe).

def automate_notepad():
    print("!!! WARNING: GIVING UP MOUSE CONTROL IN 3 SECONDS !!!")
    print("Move mouse quickly to any corner of screen to abort.")
    time.sleep(3)
    
    # 1. Open Notepad (using Windows Run)
    print("Opening Notepad...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    time.sleep(2) # Wait for app to open
    
    # 2. Type text
    print("Typing text...")
    pyautogui.typewrite("Hello! This is an automated message.\n", interval=0.1)
    pyautogui.typewrite("We are controlling the keyboard directly.\n", interval=0.1)
    pyautogui.typewrite("This is useful for legacy apps.", interval=0.1)
    
    # 3. Save File
    print("Saving file...")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite('automated_note.txt')
    pyautogui.press('enter')
    
    # Handle "Confirm Save As" if file exists (optional logic)
    time.sleep(1)
    if os.path.exists('automated_note.txt'):
         # Assuming 'Yes' is the default button or focused
         pyautogui.press('y') 

    print("Automation Complete.")

if __name__ == "__main__":
    # Requirement: pip install pyautogui
    # PyAutoGUI FailSafe: Drag mouse to corner to stop script
    pyautogui.FAILSAFE = True
    
    # Only run if user confirms
    print("This script will open Notepad and type text.")
    response = input("Type 'yes' to proceed: ")
    if response.lower() == 'yes':
        automate_notepad()
    else:
        print("Aborted.")
