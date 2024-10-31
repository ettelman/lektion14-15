from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/js/")
driver.implicitly_wait(2)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, 'text').text
    author = quote.find_element(By.CLASS_NAME, 'author').text
    print(f"{text} - by: {author}")

driver.quit