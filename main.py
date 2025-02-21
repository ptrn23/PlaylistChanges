import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, scope="playlist-read-private"))

def format_playlist(playlist_id, include_artist=True):
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']
    
    formatted_text = f"On Repeat — ptrn23\n\n"

    for i, item in enumerate(tracks, 1):
        track = item['track']
        track_name = track['name']
        artist_name = ', '.join(artist['name'] for artist in track['artists'])
        
        if include_artist:
            formatted_text += f"#{i} (=): {track_name} — {artist_name}\n"
        else:
            formatted_text += f"#{i} (=): {track_name}\n"

    return formatted_text

def save_playlist_to_file(playlist_id, include_artist=True, filename="on_repeat.txt"):
    formatted_text = format_playlist(playlist_id, include_artist)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(formatted_text)
    print(f"Playlist saved to {filename}")

playlist_id = "1CDw8ZCcssjMiCxnyWsYlA"
save_playlist_to_file(playlist_id, include_artist=False)
