from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use webdriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname_input = driver.find_element(By.NAME, 'fName')
lname_input = driver.find_element(By.NAME, 'lName')
email_input = driver.find_element(By.NAME, 'email')
submit_btn = driver.find_element(By.CLASS_NAME, 'btn')

fname_input.send_keys('John')
lname_input.send_keys('Smith')
email_input.send_keys('John.Smith@gmail.com')

submit_btn.click()

time.sleep(2)
driver.quit()