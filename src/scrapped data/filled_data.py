import pandas as pd
import requests
import base64
import time
from tqdm import tqdm
from dotenv import load_dotenv
import os

def get_access_token(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_auth_str}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    if r.status_code != 200:
        raise Exception("Could not authenticate with Spotify API")
    return r.json()["access_token"]


def fetch_track_data(track_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Failed to fetch {track_id}: {r.status_code} - {r.text}")
        return None
    return r.json()


def fetch_artist_genres(artist_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers)
    if r.status_code != 200:
        return None
    data = r.json()
    return data.get("genres", [])


load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

df = pd.read_csv("spotify-jrock-eurock/data/combined_tracks_all.csv")
df = df.drop_duplicates(subset="Track ID")
df.reset_index(drop=True, inplace=True)

df['Artist ID'] = df['Artist ID'].astype(str)
df['Release date'] = pd.to_datetime(df['Release date'], errors='coerce')

columns_to_fill = ["Artist ID", "Release date", "Genre", "Popularity", "Explicit"]

access_token = get_access_token(client_id, client_secret)

for idx, row in tqdm(df.iterrows(), total=len(df)):
    track_id = row["Track ID"]

    if pd.isna(track_id) or not isinstance(track_id, str) or len(track_id.strip()) == 0:
        continue

    needs_update = any(pd.isna(row[col]) for col in columns_to_fill)

    try:
        data = fetch_track_data(track_id, access_token)

        if not data:
            continue

        if data["artists"]:
            df.at[idx, "Artist ID"] = data["artists"][0]["id"]

        if pd.isna(row["Popularity"]):
            df.at[idx, "Popularity"] = data.get("popularity")

        if pd.isna(row["Explicit"]):
            df.at[idx, "Explicit"] = bool(data.get("explicit"))

        if data.get("album", {}).get("release_date"): 
            df.at[idx, "Release date"] = data["album"]["release_date"]

        if data["artists"]:
            artist_id = data["artists"][0]["id"]
            genres = fetch_artist_genres(artist_id, access_token)
            if genres:
                df.at[idx, "Genre"] = genres[0]

        time.sleep(0.1)

    except Exception as e:
        print(f"Error with track {track_id}: {e}")
        continue

df.to_csv("spotify-jrock-eurock/data/filled_spotify_data.csv", index=False)
print("Saved in 'filled_spotify_data.csv'")