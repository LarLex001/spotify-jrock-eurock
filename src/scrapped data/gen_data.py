import os
import ast
import pandas as pd

def clean_artist_cell(cell):
    """Clean and normalize artist cell to return a list of artist names"""
    
    if not isinstance(cell, str):
        return []
    cell = cell.strip()

    if cell.startswith("[") and cell.endswith("]"):
        try:
            parsed = ast.literal_eval(cell)
            if isinstance(parsed, list):
                return [str(a).strip() for a in parsed]
        except (SyntaxError, ValueError) as e:
            pass
    
    return [cell]


def filter_artists_from_file(df, artist_columns, target_artists):
    """Filter dataframe to keep only rows with target artists"""

    for column in artist_columns:
        if column in df.columns:
            df_copy = df.copy()
            df_copy[column] = df_copy[column].apply(clean_artist_cell)
            df_copy = df_copy.explode(column)
            df_copy = df_copy[df_copy[column].isin(target_artists)]
            if not df_copy.empty:
                return df_copy
    return pd.DataFrame() 


def process_all_files(input_dir, output_dir, artist_columns, all_artists):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            full_path = os.path.join(input_dir, file)
            try:
                df = pd.read_csv(full_path)
                filtered_df = filter_artists_from_file(df, artist_columns, all_artists)
                if not filtered_df.empty:

                    def assign_region(artist):
                        if artist in artists_list_japan:
                            return "Japan"
                        elif artist in artists_list_europe:
                            return "Europe"
                        return "Unknown"

                    for column in artist_columns:
                        if column in filtered_df.columns:
                            if filtered_df[column].apply(lambda x: isinstance(x, str)).any():
                                filtered_df["region"] = filtered_df[column].apply(assign_region)
                                break

                    output_filename = f"filtered_{file}"
                    output_path = os.path.join(output_dir, output_filename)
                    filtered_df.to_csv(output_path, index=False)
                    print(f"Saved {len(filtered_df)} lines in '{output_filename}'")
                else:
                    print(f"No suitable artist in '{file}'")
            except Exception as e:
                print(f"File error {file}: {e}")


def check_artists_in_df(df, filename, artist_column, artist_list, region_name):
    if artist_column not in df.columns:
        return  

    exploded = df.copy()
    exploded[artist_column] = exploded[artist_column].apply(clean_artist_cell)
    exploded = exploded.explode(artist_column)

    matched_df = exploded[exploded[artist_column].isin(artist_list)]
    artist_counts = matched_df[artist_column].value_counts()

    print(f"\n [{region_name}] Checking artists in '{filename}' (column: '{artist_column}')")
    for artist in artist_list:
        if artist in artist_counts:
            print(f" {artist}: {artist_counts[artist]} track(s)")
        else:
            print(f" {artist} — not found")


def analyze_and_check_all(path, artist_columns, artist_lists_dict):
    print(f"Scanning directory: {path}")

    for file in os.listdir(path):
        if file.endswith(".csv"):
            full_path = os.path.join(path, file)
            try:
                df = pd.read_csv(full_path)
                print(f"\n File: {file}")
                print(f"Rows: {len(df)}")
                print(f"Columns: {len(df.columns)}")
                print(f"Column names: {list(df.columns)}")

                for column in artist_columns:
                    for region_name, artists in artist_lists_dict.items():
                        check_artists_in_df(df, file, column, artists, region_name)

            except Exception as e:
                print(f"Failed to read {file}: {e}")


artists_list_europe = [
    "Muse", "Radiohead", "Queen", "Pink Floyd", "U2", 
    "The Cranberries", "The Police", "The Rolling Stones", "Deep Purple", "Led Zeppelin",
    "Franz Ferdinand", "Arctic Monkeys"

]
artists_list_japan = [
    "Ling tosite sigure", "Sayuri", "SID", "ASIAN KUNG-FU GENERATION", "THE ORAL CIGARETTES", 
    "KANA-BOON", "MY FIRST STORY", "WagakkiBand", "FLOW", "Aimer",
    "LiSA", "ONE OK ROCK"
]

artist_columns = ["artists", "artist_name", "track_artist"]
all_target_artists = artists_list_europe + artists_list_japan

artist_lists = {
    "Europe": artists_list_europe,
    "Japan": artists_list_japan
}

input_directory = "spotify-jrock-eurock/data/original_data/"
output_directory = "spotify-jrock-eurock/data/filtered_data/"

analyze_and_check_all(input_directory, artist_columns, artist_lists)
process_all_files(input_directory, output_directory, artist_columns, all_target_artists)
