import requests
import bs4
import pathlib
import datetime
import re

BASE_URL = "https://data.sanjoseca.gov/dataset/police-calls-for-service"
DATA_DIR = pathlib.Path("data/raw")
DOWNLOAD_CHUNK_SIZE = 8192
CURRENT_YEAR = str(datetime.datetime.now().year)

DATA_DIR.mkdir(parents=True, exist_ok=True)

def is_historical_file_already_present(filepath, filename):
    return filepath.exists() and CURRENT_YEAR not in filename

def stream_download_to_disk(url, filepath):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
            f.write(chunk)

def synchronize_resource(url, filename):
    filepath = DATA_DIR / filename
    
    if is_historical_file_already_present(filepath, filename):
        print(f"Skipping {filename} (already exists)")
        return

    print(f"Downloading {filename}...")
    stream_download_to_disk(url, filepath)

def get_portal_resource_links(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('a', class_='resource-url-analytics')

def is_annual_police_calls_csv(url, filename):
    if not url or not url.endswith('.csv'):
        return False
    return bool(re.search(r'policecalls\d{4}', filename.lower()))

def main():
    print(f"Connecting to San Jose Open Data portal...")
    resources = get_portal_resource_links(BASE_URL)
    
    sync_count = 0
    for res in resources:
        url = res.get('href')
        filename = url.split('/')[-1] if url else ""
        
        if is_annual_police_calls_csv(url, filename):
            synchronize_resource(url, filename)
            sync_count += 1
                
    print(f"\nSynchronization complete. {sync_count} files processed.")

if __name__ == "__main__":
    main()
