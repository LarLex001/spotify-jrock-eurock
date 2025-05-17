
**Тема:** Аналіз звучання J-Rock і Європейського року через аудіофічі Spotify
**Мета:**
	Дослідити, чим відрізняються композиції японського і європейського року з точки зору ритму, енергії, "сумності", динаміки.  
**Виявити:** чи можна вгадати регіон за фічами? Як кластери фіч відповідають культурним стилям?

# Списки артистів

**Японіські гурти:**

1. Ling tosite sigure
2. Sayuri
3. SID
4. ASIAN KUNG-FU GENERATION
5. THE ORAL CIGARETTES
6. KANA-BOON
7. MY FIRST STORY
8. WagakkiBand
9. FLOW
10. Aimer
11. LiSA
12. ONE OK ROCK

**Європейські гурти:**

1. Muse (UK)
2. Radiohead (UK)
3. Queen (UK)
4. Pink Floyd (UK)
5. U2 (Ireland)
6. The Cranberries (Ireland)
7. The Police (UK)
8. The Rolling Stones (UK)
9. Led Zeppelin (UK)
10. Deep Purple (UK)
11. Franz Ferdinand (Scotland)
12. Arctic Monkeys (UK)

# Аудіо-фічі Spotify

| Ознака               | Опис                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Artist ID**        | Унікальний ідентифікатор виконавця на Spotify.                                                                    |
| **Artist name**      | Ім’я виконавця або гурту.                                                                                         |
| **Region**           | Регіон/країна, де трек зібраний або вважається популярним.                                                        |
| **Track ID**         | Унікальний ідентифікатор треку на Spotify.                                                                        |
| **Track name**       | Назва пісні/трека.                                                                                                |
| **Release date**     | Дата виходу треку або альбому.                                                                                    |
| **Genre**            | Жанр музики, з яким пов’язаний виконавець чи трек.                                                                |
| **Popularity**       | Рейтинг популярності треку (від 0 до 100), розраховується Spotify на основі кількості відтворень, лайків тощо.    |
| **Explicit**         | Вказує, чи має трек ненормативну лексику або вміст `True/False`.                                                  |
| **Duration**         | Тривалість треку у секундах.                                                                                      |
| **Acousticness**     | Ймовірність того, що трек є акустичним (від 0.0 до 1.0).                                                          |
| **Danceability**     | Наскільки трек підходить для танців — базується на ритмі, темпі, стабільності (0.0–1.0).                          |
| **Energy**           | Енергетичність треку — відчуття інтенсивності й активності (0.0–1.0).                                             |
| **Instrumentalness** | Ймовірність того, що трек є інструментальним (високі значення ≈ мало вокалу).                                     |
| **Key**              | Тональність треку, як правило в числовому вигляді (0–11), що відповідає C, C#, ..., B.                            |
| **Liveness**         | Визначає ймовірність того, що трек записаний наживо (0.0–1.0).                                                    |
| **Loudness**         | Середня гучність треку в децибелах (дБ). Негативне значення.                                                      |
| **Mode**             | Лад: мажор або мінор (0 = мінор, 1 = мажор).                                                                      |
| **Speechiness**      | Визначає наявність мови/мовлення в треку (0.0–1.0). Високі значення означають треки, де є багато розмов або репу. |
| **Tempo**            | Темп треку в ударах за хвилину (BPM).                                                                             |
| **Valence**          | Міра "позитивності" треку (0.0 = сумний, 1.0 = веселий, позитивний настрій).                                      |

# Check-list артистів

**Японскі гурти (12):**

| Є/Немає | Гурти                           | dataset | SpotifyFeatures | spotify_songs | tracks_features |
| ------- | ------------------------------- | ------- | --------------- | ------------- | --------------- |
| +       | Ling tosite sigure              | 2       | 65              | -             | -               |
| -       | X JAPAN                         | 8       | -               | -             | -               |
| +       | Sayuri                          | 12      | 3               | -             | 15              |
| +       | SID                             | 9       | 25              | -             | 22              |
| -       | Supercell                       | -       | -               | -             | -               |
| +       | ASIAN KUNG-FU GENERATION        | 27      | 153             | -             | 134             |
| +       | THE ORAL CIGARETTES             | 4       | 64              | -             | -               |
| +       | KANA-BOON                       | 16      | 56              | -             | 2               |
| +       | MY FIRST STORY                  | 6       | 72              | -             | -               |
| +       | WagakkiBand                     | -       | 74              | -             | -               |
| -       | JYOCHO                          | -       | -               | -             | -               |
| +       | FLOW                            | 11      | 79              | -             | 75              |
| +       | Aimer                           | 39      | 115             | -             | 59              |
| +       | LiSA                            | 34      | 86              | -             | 100             |
| +       | ONE OK ROCK                     | 57      | 3               | 17            | 43              |
| -       | ZUTOMAYO                        | 6       | -               | -             | -               |
| -       | Fear, and Loathing in Las Vegas | 15      | 69              | -             | 11              |
| -       | asphyxia                        | -       | -               | -             | -               |
| -       | frederic                        | 3       | -               | -             | -               |
| -       | 9mm Parabellum Bullet           | 18      | -               | -             | -               |

**Європейський рок (12):**

| Є/Немає | Гурти              | Країна   | dataset | SpotifyFeatures | spotify_songs | tracks_features |
| ------- | ------------------ | -------- | ------- | --------------- | ------------- | --------------- |
| +       | Muse               | UK       | -       | 40              | 28            | 77              |
| +       | Radiohead          | UK       | 20      | 211             | 16            | 224             |
| +       | Queen              | UK       | 8       | 97              | 136           | 9               |
| +       | Pink Floyd         | UK       | 89      | 56              | 23            | 126             |
| +       | U2                 | Ireland  | -       | 18              | 32            | 10              |
| +       | The Cranberries    | Ireland  | 18      | 11              | 45            | -               |
| -       | Tokio Hotel        | Germany  | -       | -               | -             | -               |
| -       | Poets of the Fall  | Finland  | 7       | 2               | -             | -               |
| -       | Okean Elzy         | Ukraine  | -       | -               | -             | -               |
| -       | Måneskin           | Italy    | 12      | -               | 1             | 2               |
| +       | The Police         | UK       | 8       | 28              | 16            | 2               |
| -       | Billy Idol         | UK       | 7       | 15              | 10            | 3               |
| +       | The Rolling Stones | UK       | 60      | 34              | 38            | 4               |
| +       | Led Zeppelin       | UK       | 25      | 76              | 35            | 105             |
| +       | Deep Purple        | UK       | 39      | 37              | 20            | 73              |
| -       | Coldplay           | UK       | 12      | 21              | 48            | 95              |
| +       | Franz Ferdinand    | Scotland | 3       | 17              | 6             | 94              |
| +       | Arctic Monkeys     | UK       | 152     | 129             | 9             | 66              |

# Аналіз обраних датасетів

🗂️ File: dataset.csv
📊 Rows: 114000
🔢 Columns: 21
📌 Column names: ['Unnamed: 0', 'track_id', 'artists', 'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 'track_genre']

🗂️ File: SpotifyFeatures.csv
📊 Rows: 232725
🔢 Columns: 18
📌 Column names: ['genre', 'artist_name', 'track_name', 'track_id', 'popularity', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence']

🗂️ File: spotify_songs.csv
📊 Rows: 32833
🔢 Columns: 23
📌 Column names: ['track_id', 'track_name', 'track_artist', 'track_popularity', 'track_album_id', 'track_album_name', 'track_album_release_date', 'playlist_name', 'playlist_id', 'playlist_genre', 'playlist_subgenre', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

🗂️ File: tracks_features.csv
📊 Rows: 1204025
🔢 Columns: 24
📌 Column names: ['id', 'name', 'album', 'album_id', 'artists', 'artist_ids', 'track_number', 'disc_number', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'year', 'release_date']

## **Аналіз features** 

| Назви фіч        | dataset          | SpotifyFeatures  | spotify_songs            | tracks_features  |
| ---------------- | ---------------- | ---------------- | ------------------------ | ---------------- |
| Artist ID        | -                | -                | -                        | artist_ids       |
| Artist name      | artists          | artist_name      | track_artist             | artists          |
| Track ID         | track_id         | track_id         | track_id                 | id               |
| Track name       | track_name       | track_name       | track_name               | name             |
| Release date     | -                | -                | track_album_release_date | release_date     |
| Genre            | track_genre      | genre            | -                        | -                |
| Popularity       | popularity       | popularity       | track_popularity         | -                |
| Explicit         | explicit         | -                | -                        | explicit         |
| Duration         | duration_ms      | duration_ms      | duration_ms              | duration_ms      |
| Acousticness     | acousticness     | acousticness     | acousticness             | acousticness     |
| Danceability     | danceability     | danceability     | danceability             | danceability     |
| Energy           | energy           | energy           | energy                   | energy           |
| Instrumentalness | instrumentalness | instrumentalness | instrumentalness         | instrumentalness |
| Key              | key              | key              | key                      | key              |
| Liveness         | liveness         | liveness         | liveness                 | liveness         |
| Loudness         | loudness         | loudness         | loudness                 | loudness         |
| Mode             | mode             | mode             | mode                     | mode             |
| Speechiness      | speechiness      | speechiness      | speechiness              | speechiness      |
| Tempo            | tempo            | tempo            | tempo                    | tempo            |
| Valence          | valence          | valence          | valence                  | valence          |

