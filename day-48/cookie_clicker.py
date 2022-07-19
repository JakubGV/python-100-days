from selenium import webdriver
from selenium.webdriver.common.by import By

class CookieClicker:

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.driver.get('http://orteil.dashnet.org/experiments/cookie/')

    def click_cookie(self):
        cookie = self.driver.find_element(By.ID, 'cookie')
        cookie.click()

    def get_num_cookies(self):
        money_tag = self.driver.find_element(By.ID, 'money')
        return int(money_tag.text)

    def get_cookies_psec(self):
        cps_tag = self.driver.find_element(By.ID, 'cps')
        return int(cps_tag.text.split(' ')[-1])

    def buy_best_upgrade(self):
        num_cookies = self.get_num_cookies()
        
        purchase_list = self.driver.find_elements(By.CSS_SELECTOR, '#store div[id^="buy"]')
        cost_list = self.driver.find_elements(By.CSS_SELECTOR, '#store b')
        
        purchase_list = purchase_list[:8] # Only grab first 8 which are visible
        cost_list = cost_list[:8]

        prices = []
        for cost in cost_list:
            prices.append(int(cost.text.split(' ')[-1].replace(',', '')))

        for i in range(len(prices) - 1, -1, -1):
            if num_cookies > prices[i]:
                purchase_list[i].click()
                break