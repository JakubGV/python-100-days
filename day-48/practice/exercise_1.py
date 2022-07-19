from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Use webdriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.python.org')

times = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
events = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')

time_strs = [time.text for time in times]
event_strs = [event.text for event in events]

i = 0
event_dict = {}
for time, event in zip(time_strs, event_strs):
    event_dict[i] = {
        'time': time,
        'name': event
    }
    i += 1

print(event_dict)

driver.quit()