from audioop import add
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests

# Get the contents of the San Fransico Zillow apartments
zillow_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
r = requests.get(zillow_URL, headers={ 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
                                       'accept-language': 'en-US'})
contents = r.text

# Parse with BeautifulSoup
soup = BeautifulSoup(contents, 'lxml')

listings = soup.select('div#grid-search-results ul li')

links = []
prices = []
addresses = []
for listing in listings:
    link = listing.find(name='a')
    if link is not None:
        link = link.get('href')
        links.append(link)
    
    price = listing.find(name='span', attrs={'data-test': 'property-card-price'})
    if price is not None:
        if '+' in price:
            price = price[:price.index('+')]
        else:
            price = price[:price.index('/')]
        prices.append(price)
    
    address = listing.find(name='address')
    if address is not None:
        address = address.text
        addresses.append(address)

print(links)
print(prices)
print(addresses)



form_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSf0vwtuFY157GAMsGrPzPWT8op9XpI1TP_cUy_I7bCJTOQ3QQ/viewform?usp=sf_link'