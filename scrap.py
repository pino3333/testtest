import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_urls_recursive(start_url, max_depth=3):
    visited_urls = set()
    return _get_urls_recursive_helper(start_url, visited_urls, max_depth)

def _get_urls_recursive_helper(url, visited_urls, max_depth):
    if max_depth == 0:
        return []

    print(f"Scraping: {url}")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error while accessing {url}: {e}")
        return []

    if response.status_code != 200:
        print(f"Error: {response.status_code} - Unable to access {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    visited_urls.add(url)

    urls = []
    for link in soup.find_all('a', href=True):
        new_url = urljoin(url, link['href'])
        if new_url not in visited_urls:
            urls.append(new_url)
    
    for new_url in urls:
        visited_urls.update(_get_urls_recursive_helper(new_url, visited_urls, max_depth - 1))

    return visited_urls

if __name__ == "__main__":
    start_url = "https://kino-code.work/python-super-basic-course/"  # 開始URLを指定してください
    max_depth = 3  # 再帰の深さを指定してください

    result_urls = get_urls_recursive(start_url, max_depth)
    print("Collected URLs:")
    for url in result_urls:
        print(url)

##################################以下　再帰防止
def get_urls_recursive(start_url, max_depth=3):
    visited_urls = set()
    return _get_urls_recursive_helper(start_url, visited_urls, max_depth)

def _get_urls_recursive_helper(url, visited_urls, max_depth):
    if max_depth == 0 or url in visited_urls:
        return []

    print(f"Scraping: {url}")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error while accessing {url}: {e}")
        return []

    if response.status_code != 200:
        print(f"Error: {response.status_code} - Unable to access {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    visited_urls.add(url)

    urls = []
    for link in soup.find_all('a', href=True):
        new_url = urljoin(url, link['href'])
        if new_url not in visited_urls:
            urls.append(new_url)
    
    for new_url in urls:
        visited_urls.update(_get_urls_recursive_helper(new_url, visited_urls, max_depth - 1))

    return visited_urls
