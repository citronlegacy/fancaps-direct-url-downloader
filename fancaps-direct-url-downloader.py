# Fancaps Direct URL Downloader
#
# This script downloads a list of direct image URLs from Fancaps.
# Inspired by KitsunekoFi's fancaps-dl (https://github.com/KitsunekoFi/fancaps-dl),
# which is a more elaborate downloader supporting episodes and movie URLs.
#
# Usage:
#   - Paste your image URLs in the 'urls_text' multiline string.
#   - Set your preferred output folder.
#   - Run the script.

import os
import concurrent.futures
import urllib.request

# -------------------------
# User Configuration
# -------------------------

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# Paste your URLs here (one URL per line)
urls_text = """
https://cdni.fancaps.net/file/fancaps-movieimages/4839637.jpg
https://cdni.fancaps.net/file/fancaps-movieimages/4839642.jpg
https://cdni.fancaps.net/file/fancaps-movieimages/4839650.jpg
"""

# Output folder for downloaded images
OUTPUT_FOLDER = "./downloads/test3"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -------------------------
# Parse URLs
# -------------------------

image_urls = [line.strip() for line in urls_text.strip().split('\n') if line.strip()]

# -------------------------
# HTTP headers
# -------------------------

headers = {
    'User-Agent': USER_AGENT
}

# If needed, add cf_clearance cookie to headers like this:
# cf_clearance = "your_cf_clearance_cookie_here"
# headers['Cookie'] = f'cf_clearance={cf_clearance}'

# -------------------------
# Download function
# -------------------------

def download_file(url):
    filename = os.path.basename(url)
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    print(f"Downloading: {url} -> {filepath}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as out_file:
            out_file.write(resp.read())
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")

# -------------------------
# Run downloads in parallel
# -------------------------

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(download_file, image_urls)

print("🎉 Done downloading all images.")
