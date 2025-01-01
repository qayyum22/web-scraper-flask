import requests
from bs4 import BeautifulSoup

def fetch_with_proxies(url, proxies):
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    return title

# Example usage:
proxies = {
    'http': 'http://103.199.214.48',
    'http': 'http://103.41.32.185',
}
url = 'https://www.tensorflow.org/'
content = fetch_with_proxies(url, proxies)
if content:
    title = get_title(content)
    print(title)