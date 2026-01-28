import requests
import time
from plyer import notification

# STRATEGY: API Polling & Desktop Notifications
# This script demonstrates how to interact with a REST API periodically (Polling)
# and interact with the local Operating System to trigger notifications.
# Concepts: JSON Parsing, Infinite Loops, System Tray Notifications.

TARGET_PRICE = 50000 # Example target USD
COIN_ID = 'bitcoin'

def get_price():
    # Fetching data from CoinGecko Public API
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return data[COIN_ID]['usd']
    except Exception as e:
        print(f"API Error: {e}")
        return None

def main():
    print(f"Started tracking {COIN_ID} price...")
    print(f"Target Alert Price: ${TARGET_PRICE}")
    
    while True:
        price = get_price()
        
        if price:
            print(f"Current Price: ${price}")
            
            # Simple Logic: Alert if price matches criteria
            # In a real interview, discuss 'Debouncing' (don't spam alerts)
            if price > TARGET_PRICE:
                notification.notify(
                    title=f"{COIN_ID.upper()} Price Alert!",
                    message=f"Price has hit ${price}!",
                    timeout=10
                )
        
        # Wait for 60 seconds before next check
        # Strategy: Sleep prevents CPU overuse and API rate limiting
        time.sleep(60)

if __name__ == "__main__":
    # Requirement: pip install requests plyer
    main()
