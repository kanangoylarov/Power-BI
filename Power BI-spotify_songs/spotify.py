import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set up your credentials
client_id = ''
client_secret = ''

scope = 'user-read-private playlist-read-private'
# Authentication
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Load your CSV file
spotify_data = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Function to fetch album cover URL
def get_album_cover_url(track_name, artist_name):
    try:
        results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track', limit=1)
        tracks = results.get('tracks', {}).get('items', [])
        if tracks:
            return tracks[0]['album']['images'][0]['url']  # Return the URL of the first album cover
        return None
    except:
        return None

# Add a new column for the album cover URL
spotify_data['album_cover_url'] = spotify_data.apply(lambda row: get_album_cover_url(row['track_name'], row['artist(s)_name']), axis=1)

# Save the updated DataFrame to a new CSV file
spotify_data.to_csv('spotify.csv', index=False)

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import json

# # Replace with your actual client ID and client secret
# client_id = 'a8ab4474bbed4bb5b2244c4dc7875047'
# client_secret = '0639c212acb6473b81d36c9d2a60cd9f'

# # Set up the Spotify client using Client Credentials
# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(auth_manager=auth_manager)

# # Example: Search for a track (no user-specific data, just public info)
# track_name = "Columbia"
# artist_name = "Quevedo"
# results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track', limit=1)

# # Convert the results to JSON format
# results_json = json.dumps(results, indent=4)

# # Print or use the JSON data
# print(results_json)

