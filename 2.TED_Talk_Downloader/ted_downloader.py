import requests  # getting content of the TED Talk page
from bs4 import BeautifulSoup  # parsing HTML content
import re # regular expressions for text processing
import json # working with JSON data

import sys # system-specific parameters and functions

# URL of the TED Talk page
url="https://www.ted.com/talks/sir_ken_robinson_do_schools_kill_creativity"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

print(f"Connecting to TED...")
try:
    response=requests.get(url, headers=headers)
    response.raise_for_status()
    print("Connection successful.")
except Exception as e:
    print(f"Error connecting to TED: {e}")
    sys.exit()


# Find the script tag that contains the video metadata
# Modern TED pages use a JSON object inside a script tag to store video information
soup=BeautifulSoup(response.content, 'html.parser')
script_tag=soup.find("script", id="__NEXT_DATA__")

if script_tag:
    data=json.loads(script_tag.string)

    # Navigate the JSON structure to find the video URL
    # Note: The exact path in the JSON can change, but typically it is nested under props -> pageProps -> talk -> media -> resources
    try:
        # Access pageProps safely
        page_props = data.get('props', {}).get('pageProps', {})
        
        # TED updated: Title is often here now
        talk_title = page_props.get('videoData', {}).get('title', 'TED_Talk')
        
        # Look for download links
        # Structure: pageProps -> videoData -> nativeDownloads
        video_data = page_props.get('videoData', {})
        downloads = video_data.get('nativeDownloads', {})

        # Attempt to get the highest quality available
        mp4_url = downloads.get('high') or downloads.get('medium') or downloads.get('low')

        if not mp4_url:
            # Fallback for older structures
            mp4_url = video_data.get('resources', {}).get('h264', [{}])[0].get('file')

        if not mp4_url:
            print("Could not find an MP4 URL. The video might be restricted or using HLS.")
            sys.exit()

        # Clean filename
        clean_title = re.sub(r'[^\w\s-]', "", talk_title).strip().replace(" ", "_")
        file_name = f"{clean_title}.mp4"

        print(f"Talk Found: {talk_title}")
        print(f"Preparing download...")
        
        # --- STREAMING DOWNLOAD ---
        with requests.get(mp4_url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            downloaded = 0
            
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024): # 1MB chunks
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        # Calculate progress percentage
                        percent = (downloaded / total_size) * 100
                        mb_done = downloaded / (1024 * 1024)
                        mb_total = total_size / (1024 * 1024)
                        
                        # Terminal status bar
                        sys.stdout.write(f"\r[Progress: {percent:.1f}%] {mb_done:.1f}/{mb_total:.1f} MB downloaded...")
                        sys.stdout.flush()
        
        print(f"\n[+] Success! Video saved as: {file_name}")


    except (KeyError, TypeError) as e:
        print(f"Metadata structure has changed or is missing: {e}")

else:
    print("Failed to find metadata script tag.")




    
