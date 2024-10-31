from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

driver = webdriver.Chrome()

driver.get('https://webscraper.io/test-sites/e-commerce/static')

# elements = driver.find_elements(By.CLASS_NAME, 'price')

# for element in elements:
#     print(element.text)

# element = driver.find_element(By.CLASS_NAME, 'title')

# element.click()

# driver.back()
# driver.forward()
# driver.refresh()

# input_field = driver.find_elment(By.NAME, 'username')
# input_field.send_keys("username")

# input_field.submit()

# driver.implicitly_wait(5)

# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

# driver.delete_cookie('session_id')

# driver.delete_all_cookoies()

# driver.quit()

# alert = driver.switch_to.alert
# alert.send_keys()
# alert.accept()
# alert.dismiss()

driver.save_screenshot('scr.png')

element = driver.find_element(By.CLASS_NAME, 'price')
element.screenshot("elementscreenshot.png")