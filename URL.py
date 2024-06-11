import requests
import time

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    urls = [
        'https://example.com/file1.zip',
        'https://example.com/file2.zip',
        'https://example.com/file3.zip',
        'https://example.com/file4.zip',
        'https://example.com/file5.zip',
        'https://example.com/file6.zip',
        'https://example.com/file7.zip',
        'https://example.com/file8.zip',
        'https://example.com/file9.zip',
        'https://example.com/file10.zip'
    ]
    start_time = time.time()
    
    for i, url in enumerate(urls):
        download_file(url, f'file{i + 1}.zip')
    
    end_time = time.time()
    print(f"Tempo total sem threads: {end_time - start_time:.2f} segundos")
""