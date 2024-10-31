from bs4 import BeautifulSoup
import requests
import re

url = "https://webscraper.io/test-sites/e-commerce/static"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'lxml')

# title_tag = soup.title
# body_tag = soup.body
# next_sibling = body_tag.next_sibling

# print(next_sibling)
# for child in body_tag.children:
#     print(child)

# div_tag = soup.find('div')
# div_tags = soup.find_all('div', class_='')
# print(div_tag)

# headers = soup.find_all(re.compile('^h[1-6]$'))

# print(headers)

title_tag = soup.title
div_tag = soup.find('div')
print(div_tag.get_text())