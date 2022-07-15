import requests
from bs4 import BeautifulSoup

# Get input from the user on the year to search
travel_date_str = input("Which year do you want to travel to? " \
                        "Type the date in this format YYYY-MM-DD: ")
year = travel_date_str[:4]

# Get the Billboard top 100 for that date
url = f"https://www.billboard.com/charts/hot-100/{travel_date_str}"
response = requests.get(url)
charts_text = response.text

# Parse the list to get the song names
soup = BeautifulSoup(charts_text, 'html.parser')

charts_html = soup.find(name='div', class_='chart-results-list')
rows_html = soup.find_all(name='div', class_='o-chart-results-list-row-container')

title_tags = []
for row in rows_html:
    title_tags.append(row.find(name='h3'))

titles = []
for tag in title_tags:
    titles.append(tag.getText().strip())

# Connect to Spotify
import os
from dotenv import load_dotenv
from spotify_interface import SpotifyInterface

load_dotenv()
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
redirect_uri = 'http://example.com'
scope = 'playlist-modify-private'

spotify = SpotifyInterface(client_id, client_secret, redirect_uri, scope)

song_URIs = []
for title in titles:
    uri = spotify.find_song_URI(title, year)
    if uri is not None:
        song_URIs.append(uri)

print(song_URIs)