import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_="thumbnail")

for product in products:
    product_name = product.find('a', class_='title').text.strip()
    price = product.find('h4', class_="price").text.strip()
    product_link = "https://webscraper.io" + product.find('a', class_='title')['href']

    print(f"Produktnamn: {product_name}")
    print(f"Pris: {price}")
    print(f"Länk: {product_link}")
    print('-' * 60)