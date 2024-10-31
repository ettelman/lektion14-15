from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("http://example.com")

print("Solve the captcha")
input()

html = driver.page_source

with open("webpage.html", "w", encoding='utf-8') as file:
    file.write(html)

print("Copied webpage to file")

driver.quit()