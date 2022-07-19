from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Package to send special keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use webdriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

num_articles = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')

print(f"Number of articles: {num_articles.text}")

# num_articles.click() # Click on a tag

content_portals = driver.find_element(By.LINK_TEXT, 'Content portals') # Find elements by link text
# content_portals.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python') # Type in an input tag
search_bar.send_keys(Keys.ENTER)

time.sleep(2)
driver.quit()