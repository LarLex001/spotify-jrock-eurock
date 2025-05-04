import pandas as pd
import numpy as np

final_features = [
    "Artist ID", "Artist name", "Region", "Track ID", "Track name", "Release date",
    "Genre", "Popularity", "Explicit", "Duration", "Acousticness", "Danceability",
    "Energy", "Instrumentalness", "Key", "Liveness", "Loudness", "Mode",
    "Speechiness", "Tempo", "Valence"
]

column_mappings = {
    "spotify-jrock-eurock/data/filtered_data/filtered_dataset.csv": {
        "Artist name": "artists",
        "Track ID": "track_id",
        "Track name": "track_name",
        "Genre": "track_genre",
        "Popularity": "popularity",
        "Explicit": "explicit",
        "Duration": "duration_ms",
        "Acousticness": "acousticness",
        "Danceability": "danceability",
        "Energy": "energy",
        "Instrumentalness": "instrumentalness",
        "Key": "key",
        "Liveness": "liveness",
        "Loudness": "loudness",
        "Mode": "mode",
        "Speechiness": "speechiness",
        "Tempo": "tempo",
        "Valence": "valence",
        "Region": "region"
    },
    "spotify-jrock-eurock/data/filtered_data/filtered_SpotifyFeatures.csv": {
        "Artist name": "artist_name",
        "Track ID": "track_id",
        "Track name": "track_name",
        "Genre": "genre",
        "Popularity": "popularity",
        "Duration": "duration_ms",
        "Acousticness": "acousticness",
        "Danceability": "danceability",
        "Energy": "energy",
        "Instrumentalness": "instrumentalness",
        "Key": "key",
        "Liveness": "liveness",
        "Loudness": "loudness",
        "Mode": "mode",
        "Speechiness": "speechiness",
        "Tempo": "tempo",
        "Valence": "valence",
        "Region": "region"
    },
    "spotify-jrock-eurock/data/filtered_data/filtered_spotify_songs.csv": {
        "Artist name": "track_artist",
        "Track ID": "track_id",
        "Track name": "track_name",
        "Release date": "track_album_release_date",
        "Popularity": "track_popularity",
        "Duration": "duration_ms",
        "Acousticness": "acousticness",
        "Danceability": "danceability",
        "Energy": "energy",
        "Instrumentalness": "instrumentalness",
        "Key": "key",
        "Liveness": "liveness",
        "Loudness": "loudness",
        "Mode": "mode",
        "Speechiness": "speechiness",
        "Tempo": "tempo",
        "Valence": "valence",
        "Region": "region"
    },
    "spotify-jrock-eurock/data/filtered_data/filtered_tracks_features.csv": {
        "Artist ID": "artist_ids",
        "Artist name": "artists",
        "Track ID": "id",
        "Track name": "name",
        "Release date": "release_date",
        "Explicit": "explicit",
        "Duration": "duration_ms",
        "Acousticness": "acousticness",
        "Danceability": "danceability",
        "Energy": "energy",
        "Instrumentalness": "instrumentalness",
        "Key": "key",
        "Liveness": "liveness",
        "Loudness": "loudness",
        "Mode": "mode",
        "Speechiness": "speechiness",
        "Tempo": "tempo",
        "Valence": "valence",
        "Region": "region"
    }
}

def align_dataset(df, mapping):
    aligned = pd.DataFrame()
    for col in final_features:
        if col in mapping and mapping[col] in df.columns:
            aligned[col] = df[mapping[col]]
        else:
            aligned[col] = np.nan
    return aligned

all_dfs = []

for filename, colmap in column_mappings.items():
    try:
        df = pd.read_csv(filename)
        aligned_df = align_dataset(df, colmap)
        all_dfs.append(aligned_df)
        print(f"Download '{filename}' ({len(df)} rows)")
    except Exception as e:
        print(f"Error: '{filename}': {e}")

combined_df = pd.concat(all_dfs, ignore_index=True)
combined_df.to_csv("spotify-jrock-eurock/data/combined_tracks_all.csv", index=False)
print(f"\nSuccessfully merged: {len(combined_df)} rows. Saved in 'combined_tracks_all.csv'")
