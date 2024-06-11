import requests
import threading
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
    threads = []
    start_time = time.time()
    
    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_file, args=(url, f'file{i + 1}.zip'))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Tempo total com threads: {end_time - start_time:.2f} segundos")
