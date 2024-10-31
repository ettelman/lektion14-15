import requests
from bs4 import BeautifulSoup

url = "https://aftonbladet.se"


try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error {e}")

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h3')

for heading in headings:
    print(heading.get_text())
    
