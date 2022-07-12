from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
movies_article = response.text

soup = BeautifulSoup(movies_article, 'html.parser')

title_tags = soup.find_all(name='h3', class_='title')

movies = [tag.getText() for tag in title_tags]
movies = movies[::-1] # Reverse the order of the list

with open('movies.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(movies))