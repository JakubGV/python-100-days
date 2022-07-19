from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Package to send special keys
from webdriver_manager.chrome import ChromeDriverManager
from cookie_clicker import CookieClicker
import time

PLAY_DURATION_MINS = 5 # Play for PLAY_DURATION_MINS number of minutes
BUY_INTERVAL_SECS = 5 # Buy upgrade every BUY_INTERVAL_SECS number of seconds
CLICKS_PER_SEC = 20 # Click every CLICKS_PER_SEC number of seconds

PLAY_DURATION_SECS = PLAY_DURATION_MINS * 60

def main():
    # Start the service
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Initialize cookie clicker instance
    cookie_clicker = CookieClicker(driver)

    # Initialize playing loop
    timeout_start = time.time()
    while time.time() < timeout_start + PLAY_DURATION_SECS:
        buy_timeout_start = time.time()
        while time.time() < buy_timeout_start + BUY_INTERVAL_SECS:
            cookie_clicker.click_cookie()
            time.sleep(float(1/CLICKS_PER_SEC))
        
        cookie_clicker.buy_best_upgrade()

    print(f"cookies/second: {cookie_clicker.get_cookies_psec()}")

    driver.quit()

if __name__ == '__main__':
    main()