from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# STRATEGY: Browser Automation (RPA)
# Unlike 'requests' which only gets HTML, Selenium opens a real browser.
# This is used for sites that require JavaScript, login interaction, or look-and-feel testing.
# Concepts: DOM Selection (XPath/CSS), Session Handling, WebDriver.

def login_automation():
    # Setup Chrome Driver automatically
    print("Initializing Browser...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Step 1: Navigate
        url = "https://the-internet.herokuapp.com/login"
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Step 2: Locate Elements
        # Strategy: Interact with input fields by ID
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Step 3: Action
        print("Entering credentials...")
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        
        time.sleep(1) # Pause to visualize (remove in production)
        login_btn.click()
        
        # Step 4: Verification
        time.sleep(1)
        if "You logged into a secure area!" in driver.page_source:
             print("SUCCESS: Login Verified!")
        else:
             print("FAILURE: Login functionality failed.")
             
    except Exception as e:
        print(f"Error during automation: {e}")
    finally:
        # Step 5: Cleanup
        # Always quit the driver to close the browser window
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    # Requirements: pip install selenium webdriver-manager
    login_automation()
