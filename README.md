# 🎸 European vs Japanese Rock Music Analysis

A data science project that analyses and compares the characteristics of rock music by European and Japanese artists based on the features of the Spotify API.

## 📊 Overview

This project explores musical differences between European and Japanese rock music through data analysis of Spotify tracks. It includes:
- Comprehensive analysis of the audio characteristics and musical structure of the songs
- Statistical comparisons between regions and visualisation of differences
- Clustering analysis to identify pattern groups
- Classification model to predict a track's region based on its characteristics

## 🎵 Key Features.

- **Data Collection**: Separate datasets from Kaggle are used, which have audio features of rock songs from different regions (since the Spotify [changed the API policy](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)) and the Spotify API to supplement track information
- **Data Preprocessing**: Cleaning and standardizing the dataset
- **Data analysis and visualisation:** Investigates various musical aspects including:
  - Audio characteristics (energy, valence, loudness, etc.)
  - Musical structure (Instrumentalness, Speechiness, etc.)
  - Trends in popularity
  - Song duration and key
  - Distribution by genre
- **Machine learning:**
  - Cluster analysis to identify distinct musical patterns
  - Classification model to predict the origin of tracks (Europe/Japan)

## 📈 Key Findings

- Japanese rock tends to be louder and more energetic than European rock
- European rock shows more genre diversity and has average values of audio characteristics
- The cluster analysis reveals two fairly clear clusters containing music from a particular region and a third cluster that is an intersection of rock music from different regions
- Clear regional differences in musical characteristics allow for accurate classification

## 🔗 Data Sources

  For this data analysis, we used the Spotify Web API and the following datasets from the Kaggle platform:
  - [30000 Spotify Songs](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs)
  - [Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
  - [Spotify 1.2M+ Songs](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs)
  - [🎹 Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
  
## 🗺️ Project implementation sequence

  1. **Collecting and organising data:**
	  At this stage, three scripts are executed sequentially, which:
	  1. [*gen_data:*](src/scrapped%20data/gen_data.py) extracts only the required performers from all datasets, divides them into groups and creates filtered files
	  2. [*merge_data:*](src/scrapped%20data/merge_data.py) unifies all the necessary columns and brings all the data to a single structure, combining them
	  3. [*filled_data:*](src/scrapped%20data/filled_data.py) fills in certain data, removes duplicates and saves the dataset
2. **Data preparation and cleaning:**
	[*prepeared_data:*](notebooks/prepared_data.ipynb) data is checked, cleaned and brought into a convenient form. As a result of running this notebook, two datasets are created: 
	- complete one
	- for analysis (containing a limited number of songs by artists)
3. **Data analytics and ML:**
	[*analysis_data:*](notebooks/analysis_data.ipynb) includes descriptive data analysis and data visualisation. As well as clustering and classification
4. **Use of the created model:**
	[*user_predict:*](src/classification%20model/user_predict.py) anyone can enter certain features and try to classify a rock song by region

## 📁 Project Structure

```
spotify-jrock-eurock/
├── data/
│   ├── original_data/
│   ├── filtered_data/
│   └── cleaned_data/
├── models/
├── notebooks/
│   ├── prepared_data.ipynb
│   └── analysis_data.ipynb
├── src/
│   ├── scrapped data/
│   │   ├── gen_data.py
│   │   ├── merge_data.py
│   │   └── filled_data.py
│   └── classification model/
│       └── user_predict.py
└── requirements.txt
```

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/LarLex001/spotify-jrock-eurock.git
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Set up Spotify API credentials:

   - Create a `.env` file in the root directory
   - Add your Spotify API credentials:

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

4. Run the data collection scripts in sequence:

```bash
python src/scrapped\ data/gen_data.py
python src/scrapped\ data/merge_data.py
python src/scrapped\ data/filled_data.py
```

5. Explore the Jupyter notebooks in the `notebooks/` directory for analysis.

## 🛠️ Technologies Used

- Python 3.11
- Data Analysis (pandas, numpy)
- Data Visualization (matplotlib, seaborn)
- Machine Learning (scikit-learn, XGBoost)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
