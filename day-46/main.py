import requests
from bs4 import BeautifulSoup

travel_date_str = input("Which year do you want to travel to? " \
                        "Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{travel_date_str}"
response = requests.get(url)
charts_text = response.text

soup = BeautifulSoup(charts_text, 'html.parser')

charts_html = soup.find(name='div', class_='chart-results-list')
rows_html = soup.find_all(name='div', class_='o-chart-results-list-row-container')

title_tags = []
for row in rows_html:
    title_tags.append(row.find(name='h3'))

titles = []
for tag in title_tags:
    titles.append(tag.getText().strip())

print(titles)