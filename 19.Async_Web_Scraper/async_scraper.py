import asyncio
import aiohttp
import time

# INTERVIEW QUESTION: "Your scraping script takes 10 minutes to process 100 pages. How do you make it faster?"
# Answer: "Use Asynchronous I/O (AsyncIO) to fetch pages concurrently instead of sequentially."
# This is a SENIOR/ADVANCED automation concept.

URLS = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org"
] * 10  # Simulate 50 requests

async def fetch_page(session, url, id):
    try:
        start = time.time()
        async with session.get(url) as response:
            await response.text() # Wait for body download
            end = time.time()
            print(f"[{id}] Finished {url} in {end-start:.2f}s")
            return response.status
    except Exception as e:
        print(f"[{id}] Error {url}: {e}")
        return 0

async def main_async():
    print(f"Starting ASYNC fetch of {len(URLS)} pages...")
    start_total = time.time()
    
    # Context manager for the session
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(URLS):
            # Create a 'task' (future work) for each URL
            task = asyncio.create_task(fetch_page(session, url, i))
            tasks.append(task)
        
        # Run all tasks at once
        await asyncio.gather(*tasks)

    print(f"\nTOTAL TIME (Async): {time.time() - start_total:.2f} seconds")

# --- COMPARISON (Sequential) ---
def fetch_users_sequential():
    import requests
    print(f"\nStarting SEQUENTIAL fetch (Demo of slowness)...")
    start_total = time.time()
    for i, url in enumerate(URLS[:5]): # Only do 5 to save time
        print(f"Fetching {url}...")
        requests.get(url)
    print(f"Time for just 5 sequential requests: {time.time() - start_total:.2f}s")

if __name__ == "__main__":
    # Requirement: pip install aiohttp
    import sys
    
    # Windows SelectorEventLoop Policy fix for Python 3.8+
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    # 1. Run Async (Fast)
    asyncio.run(main_async())
    
    # 2. Run Sync (Slow) - Uncomment to see the difference
    # fetch_users_sequential()
