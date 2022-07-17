import requests
from bs4 import BeautifulSoup
import logging
import os, sys
from dotenv import load_dotenv
from spotify_interface import SpotifyInterface

# Define logger
def get_logger():
    log = logging.getLogger("Billboard Spotify Playlist Maker")

    # Add timestamps to logs
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fmt = logging.Formatter()
    ch.setFormatter(fmt)
    log.addHandler(ch)

    return log

def main():
    log = get_logger()

    # Get input from the user on the year to search
    travel_date_str = input("Which year do you want to travel to? " \
                            "Type the date in this format YYYY-MM-DD: ")
    year = travel_date_str[:4]
    log.info(f"Input given: {travel_date_str}")

    # Get the Billboard top 100 for that date
    url = f"https://www.billboard.com/charts/hot-100/{travel_date_str}"
    response = requests.get(url)
    charts_text = response.text
    log.info(f"Webpage at {url} was requested")

    # Parse the list to get the song names
    soup = BeautifulSoup(charts_text, 'html.parser')

    rows_html = soup.find_all(name='div', class_='o-chart-results-list-row-container')

    title_tags = []
    for row in rows_html:
        title_tags.append(row.find(name='h3'))

    titles = []
    for tag in title_tags:
        titles.append(tag.getText().strip())
    log.info(f"{len(titles)} songs found")

    # Get the environment variables to connect to Spotify
    load_dotenv()
    client_id = os.environ['client_id']
    client_secret = os.environ['client_secret']
    redirect_uri = 'http://example.com'
    scope = 'playlist-modify-private'

    # Create a SpotifyInterface instance based on the Spotipy library
    spotify = SpotifyInterface(client_id, client_secret, redirect_uri, scope)
    log.info('SpotifyInterface instance created')

    # Get the URIs (Unique Resource Identifiers) of the songs
    song_URIs = []
    for title in titles:
        uri = spotify.find_song_URI(title, year)
        if uri is not None:
            song_URIs.append(uri)
    log.info(f"URIs found for {len(song_URIs)} songs")

    # Create private playlist
    name = f"{travel_date_str} Billboard 100"
    playlist_id = spotify.create_playlist(name, False)
    if playlist_id is not None:
        log.info(f"Playlist with name: {name} and id: {playlist_id} created")
    else:
        log.error(f"Playlist with name: {name} failed to be created")
        sys.exit(1)

    # Add songs to playlist
    snapshot_id = spotify.add_playlist_songs(playlist_id, song_URIs)
    if snapshot_id is not None:
        log.info(f"{len(song_URIs)} songs were inserted into playlist with id {playlist_id}")
    else:
        log.error(f"Failed to insert songs into playlist with id {playlist_id}")

if __name__ == '__main__':
    main()