## Table of Contents

- [Team Members](#team-members)
- [Business Overview](#business-overview)
- [Business Questions](#business-questions)
- [Dataset](#dataset)
- [Database Design](#database-design)
- [Data Preparation](#data-preparation)
- [Python Analysis](#python-analysis)
- [SQL Analysis](#sql-analysis)
- [Key Findings](#key-findings)
- [Business Recommendations](#business-recommendations)
- [Repository Structure](#repository-structure)
- [How to Run the Project](#how-to-run-the-project)

# Track Record Awards

## Team Members
- Francisco Reis
- Juan Contreras
- Marta Atencia

## Business Overview
Track Record Awards is a Spotify subsidiary that produces an annual music awards ceremony. The event brings together artists, record labels, and fans to celebrate standout music across genres. The company earns revenue through ticket sales, sponsorships, and media partnerships.

Track Record Awards hired us as independent data analysts to recommend nominees and winners for its **2026 ceremony**. Our main stakeholder is the awards committee, which needs clear, consistent criteria it can explain to artists and fans. We use Spotify data to rank eligible artists, tracks, and albums by the metric defined for each award.s

### 2026 Awards

The annual awards celebrate the artists, tracks, and albums that stood out among **2025 releases**. The three headline awards span all genres. Tracks and albums qualify by release date, and artists qualify by having at least one release in 2025.

The committee also wants to recognise standout tracks within individual music genres. **Pop, Hip-Hop, Rock, R&B, Electronic Music, and Country** each have a separate track award, with their own shortlist and winner.

- **Artist of the Year** — the eligible artist with the most Spotify followers.
- **Track of the Year** — the 2025 track with the highest Spotify popularity score across all genres.
- **Album of the Year** — the 2025 album with the highest popularity score.
- **Most Popular Track by Genre** — the highest popularity-scoring 2025 track in each of the six genres.

### 10th Anniversary Awards

To celebrate its 10th anniversary, Track Record Awards is introducing two new honors at the 2026 ceremony. The committee wants to look beyond this year’s eligible releases and celebrate the **favorite tracks of the decade** and an **all-time favourite artist**. For this retrospective, we look at music released from **2015 through 2025** (inclusive).

- **Track of the Decade by Genre** — celebrates the most popular track from the last decade in each of the six genres: Pop, Hip-Hop, Rock, R&B, Electronic Music, and Country.
- **All-Time Favorite Artist** — recognises one artist across all genres, taking into account the popularity of their releases from the anniversary period and the size of their Spotify following.

## Business Questions
We defined which artists, tracks, and albums the committee should nominate for the 2026 Track Record Awards, and how they can determine the winners of each category. Below you can  see which Spotify metrics are used and how the data is compared to inform the decision.

### 2026 Awards

The annual awards focus on music released in the last year. The headline awards compare eligible entries across all genres, while the genre awards produce a separate shortlist and winner for each genre.

- **Artist of the Year.** Which artist with at least one 2025 release has the most Spotify followers. This category recognises the artist with the largest following among those who released music that year.
- **Track of the Year.** Which track released in 2025 has the highest Spotify track popularity score across all genres.
- **Album of the Year.** Which album released in 2025 has the highest album popularity score.
- **Most Popular Pop Track.** Which 2025 Pop track has the highest popularity score among eligible Pop releases.
- **Most Popular Hip-Hop Track.** Which 2025 Hip-Hop track has the highest popularity score among eligible Hip-Hop releases.
- **Most Popular Rock Track.** Which 2025 Rock track has the highest popularity score among eligible Rock releases.
- **Most Popular R&B Track.** Which 2025 R&B track has the highest popularity score among eligible R&B releases.
- **Most Popular Electronic Music Track.** Which 2025 Electronic Music track has the highest popularity score among eligible Electronic Music releases.
- **Most Popular Country Track.** Which 2025 Country track has the highest popularity score among eligible Country releases.

### 10th Anniversary Awards

The new anniversary awards compare releases from **2015 through 2025, inclusive**. The committee wants to recognise a favourite track in each genre and one all-time favourite artist across genres.

- **Most Popular Pop Track of the Decade.** Which Pop track ranks highest by popularity across the 10-year period.
- **Most Popular Hip-Hop Track of the Decade.** Which Hip-Hop track ranks highest by popularity across the 10-year period.
- **Most Popular Rock Track of the Decade.** Which Rock track ranks highest by popularity across the 10-year period.
- **Most Popular R&B Track of the Decade.** Which R&B track ranks highest by popularity across the 10-year period.
- **Most Popular Electronic Music Track of the Decade.** Which Electronic Music track ranks highest by popularity across the 10-year period.
- **Most Popular Country Track of the Decade.** Which Country track ranks highest by popularity across the anniversary period.
- **All-Time Favorite Artist.** Which artist ranks highest when we consider both the popularity of their releases from 2015 through 2025 and the size of their Spotify following.

## Dataset
We used the [Spotify Global Music Dataset (2009–2025)](https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025), published by Warda Bilal on Kaggle. According to the dataset author, the data was collected through Spotify’s public API for educational and research purposes.

The dataset contains two CSV files with track, artist, and album information. The table shows the dimensions of each file before cleaning or merging.

| Source file | Data rows | Columns |
|---|---:|---:|
| `spotify_data_clean.csv` | 8,582 | 15 |
| `track_data_final.csv` | 8,778 | 15 |

Together, the downloaded files contain records of tracks released between 2009 and 2025. 
Note: Although the description of the dataset published on Kaggle, mentions the records excluded 2024, we have concluded, after analyzing these datasets, that the dataset does include records for releases in 2024.

We use release dates to determine award eligibility, genre labels to group tracks, and popularity scores and artist follower counts to rank entries. The 2026 annual awards focus on music released in 2025, while the 10th anniversary awards consider releases from 2015 through 2025, inclusive.

## Database Design
We designed the database in DrawDB and exported the schema as a SQL script. Both the SQL script and the DrawDB diagram image are in the project folder (first_project/sql_scripts). More detailed information can be found in the dedicated SQL section below.

## Data Preparation
We used `data_cleaning.ipynb` to combine the two source files, standardize their fields, and prepare the datasets for the annual and anniversary awards.

1. **Load and merge the source files.** We loaded `spotify_data_clean.csv` and `track_data_final.csv` into pandas and joined them on `track_id` using an outer join. This kept tracks that appeared in either file. We exported the intermediate result as `merged_spotify_data.csv`.

2. **Inspect the merged data.** We reviewed the column names and data types and compared the number of unique `track_id` values with the total row count to check for duplicate track IDs. We concluded there were no duplicated records.

3. **Consolidate overlapping fields.** The merge created two versions of fields shared by both files. We removed brackets and surrounding quotes from one of the genre columns, then filled missing values in the selected track, artist, genre, and album fields using the corresponding values from the other source.

4. **Select and rename the analysis columns.** We kept nine fields covering track ID, track name, track popularity, artist name, artist popularity, artist followers, artist genres, album name, and album release date. We removed the `_x` and `_y` suffixes added during the merge.

5. **Standardise release years and numeric fields.** We checked for missing album release dates, kept only the release year, and reviewed the distribution of records by year. We converted the release year, track popularity, artist popularity, and artist follower count to integers.

6. **Filter and export the award datasets.** We created `last_year_tracks.csv` for 2025 releases and `last_decade_tracks.csv` for releases from 2015 onward. We saved both files and the full `refined_dataset.csv` as semicolon-delimited CSVs.

7. **Map subgenres to award categories.** We split the artist genre labels into individual subgenres, trimmed spaces, and converted them to lowercase. We used keyword matching to assign the first matching category from Pop, Hip-Hop, Rock, R&B, Electronic Music, or Country. The intended fallback labels were `Unknown` for missing genres and `Other` for genres with no match. The notebook also includes an export of 2025 tracks labelled `Other` to `other_2025.csv` for review.

## Python Analysis
We used pandas in two Jupyter notebooks to rank eligible entries for the 2026 Track Record Awards. We analysed the 2025 releases first, then used the 2015–2025 dataset for the 10th anniversary awards.

### 2025 Releases (`awards_2025.ipynb`)

1. **Rank artists by followers.** After loading the dataset including all the 2025 records (`last_year_tracks.csv`), we grouped the records by artist and kept the highest recorded Spotify follower count for each artist. We displayed the top 10 with their follower counts.
2. **Rank tracks by popularity.** We grouped records by track name and artist, calculated the median track popularity for each group, rounded the scores, and ranked them from highest to lowest. We displayed the top 10.
3. **Rank albums by average track popularity.** We grouped records by album name and artist, then used the median popularity of the tracks available for each album as its score. We rounded the scores, displayed the top 10.
4. **Compare artists within each genre.** We filtered the data separately for Pop, Hip-Hop, Rock, R&B, Electronic Music, and Country. Within each genre, we calculated and rounded each artist’s median track popularity and displayed the top 10 artists.

### 10th Anniversary Awards (`awards_last_decade.ipynb`)

1. **Load the anniversary dataset.** We loaded `last_decade_tracks.csv`, which contains eligible releases from 2015 through 2025.
2. **Rank tracks within each genre.** For Pop, Hip-Hop, Rock, R&B, Electronic Music, and Country, we sorted tracks by Spotify popularity, kept one entry per track ID, and displayed the top 10 tracks with their artists and scores.
3. **Put follower counts on a 0–100 scale.** For the All-Time Favorite Track ranking, we wanted a single score that was easy to compare across nominees. Track popularity was already on a 0–100 scale, so we divided each artist’s follower count by the highest follower count in the data and multiplied by 100, the highest count receiving a score of 100.
4. **Calculate a weighted score for each track.** We gave track popularity 80% of the weight and the scaled follower score 20%. This made the track’s own popularity the main factor while still accounting for the size of the artist’s audience.

   `Favorite score = (track popularity × 0.80) + (scaled follower score × 0.20)`

5. **Select one nominee from each release window.** After calculating the combined score, we kept one entry per track ID. We then split the releases into three groups: 2015–2018, 2019–2022, and 2023–2025. Within each group, we nominated the track with the highest score. This gave us three finalists, one from each period, so the shortlist wouldn’t only include recent releases.
7. **Calculate the artist score and rank the top 10.** We scaled follower counts to 0–100 using the highest count among artists in this ranking. We applied the same weighting (80% median track popularity and 20% scaled follower score) and then sorted artists by their combined score and displayed the top 10.

## SQL Analysis
We used MySQL to create and populate a relational database based on the structure defined in our Entity Relationship Diagram (ERD). The database was designed to organise the Spotify data into related tables, reducing data duplication and establishing relationships between tracks, albums, artists, and genres.

1. **Design the database structure:** We created an ERD using DrawDB to define the database structure according to the source data and the project's requirements. This allowed us to identify the necessary tables, primary keys, foreign keys, and relationships before creating the database. Six tables were developed: albums, tracks, artists, genres, track_artist, and artist_genre. The two relationship tables use composite primary keys to manage the cardinality between tracks and artists, and artists and genres.
2. **Create the database and tables.** Based on the ERD, we exported the SQL schema and used it to create a database named `awards`. We saved the creation script in create_database, which contains the SQL statements required to create the database and its six tables. We also established foreign key constraints to connect the related tables and used `ON UPDATE CASCADE` and `ON DELETE CASCADE` to maintain referential integrity when referenced records are updated or deleted.
3. **Prepare the data for import.** Using Python, we generated separate CSV files for each database table, containing only the required columns. For tables requiring new content IDs that were not available in the original dataset, we added an incremental index generation step in Python to create unique IDs before importing the data, rather than relying on `SQL AUTO_INCREMENT`.
4. **Populate the database.** We initially attempted to import the CSV files using the MySQL Table Data Import Wizard. However, the import process encountered issues with file encoding and special characters present in some of the records. To overcome this, we created a dedicated SQL script named database_populate, using `LOAD DATA LOCAL INFILE` to import the CSV files directly into their corresponding tables. We configured the imports to use utf8mb4 encoding, semicolons as field delimiters, double quotes as text enclosures, and to skip the header rows. We also followed the table dependency order to ensure that referenced records were available before populating tables containing foreign keys.
5. **EDA and business analysis**. Although we created and populated the SQL database, all the findings required to answer the project's business questions were obtained directly through Python and pandas. Given the nature of this exploratory data analysis, there was no need to perform additional analysis using SQL.

### Annual Awards — 2025 Releases

#### Artist of the Year

| Rank | Artist | Spotify followers |
|---:|---|---:|
| 1 | Taylor Swift | 145,542,136 |
| 2 | Ed Sheeran | 122,802,777 |
| 3 | The Weeknd | 112,995,439 |

#### Track of the Year

| Track | Artist | Track popularity |
|---|---|---:|
| Golden | HUNTR/X | 99 |
| Opalite | Taylor Swift | 97 |
| Man I Need | Olivia Dean | 95 |
| Elizabeth Taylor | Taylor Swift | 95 |

#### Album of the Year

| Top-ranked release | Artist | Average track popularity |
|---|---|---:|
| Man I Need | Olivia Dean | 95 |

The ranking includes multiple release types. Album eligibility for *Man I Need* still needs to be verified.

#### 2025 Genre Awards

The current notebook ranks artists by their average track popularity within each genre. The tables below show the leading artist in each category. Individual track winners still require a track-level ranking.

##### Pop

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| HUNTR/X | 94 |

##### Hip-Hop

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| Bad Bunny | 90 |

##### Rock

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| Tame Impala | 79 |

##### R&B

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| DJ Japa NK | 85 |

##### Electronic Music

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| Disco Lines | 92 |

##### Country

| Top-ranked artist | Average track popularity (rounded) |
|---|---:|
| Taylor Swift | 91 |

### 10th Anniversary Awards — 2015–2025 Releases

#### Pop Track of the Decade

| Top-ranked track | Artist | Track popularity |
|---|---|---:|
| Golden | HUNTR/X | 99 |

#### Hip-Hop Track of the Decade

| Top-ranked track | Artist | Track popularity |
|---|---|---:|
| DtMF | Bad Bunny | 91 |

#### Rock Track of the Decade

| Top-ranked track | Artist | Track popularity |
|---|---|---:|
| Love Me Not | Ravyn Lenae | 89 |

#### R&B Track of the Decade

| Joint top-ranked track | Artist | Track popularity |
|---|---|---:|
| Posso Até Não Te Dar Flores | DJ Japa NK | 85 |
| Snooze | SZA | 85 |

#### Electronic Music Track of the Decade

| Top-ranked track | Artist | Track popularity |
|---|---|---:|
| No Broke Boys | Disco Lines | 92 |

#### Country Track of the Decade

| Top-ranked track | Artist | Track popularity |
|---|---|---:|
| Opalite | Taylor Swift | 97 |

#### All-Time Favorite Track

| Release window | Finalist | Artist | Release year | Combined score |
|---|---|---|---:|---:|
| 2015–2018 | Perfect | Ed Sheeran | 2017 | 87.27 |
| 2019–2022 | Cruel Summer | Taylor Swift | 2019 | 89.59 |
| 2023–2025 | **The Fate of Ophelia** | **Taylor Swift** | 2025 | **99.99** |

*The Fate of Ophelia* has the highest combined score among the three finalists.

#### All-Time Favorite Artist

| Rank | Artist | Median track popularity | Spotify followers | Combined score |
|---:|---|---:|---:|---:|
| 1 | Billie Eilish | 74.0 | 118,797,451 | 75.52 |
| 2 | Saja Boys | 93.5 | 2,234,812 | 75.11 |
| 3 | HUNTR/X | 92.5 | 3,568,209 | 74.49 |

## Business Recommendations
The Track Record Awards committee can use the current rankings to shortlist nominees from the available Spotify data. Before confirming winners, we recommend checking that each ranking matches the award’s eligibility rules and expanding the evidence used for future editions.

1. **Confirm what qualifies for each award.** For the 2025 genre awards, rank individual tracks within each genre. The current analysis ranks artists by their average track popularity. For Album of the Year, verify the release type so that only eligible albums enter the ranking. Agree on a tie-break rule before selecting winners, as two tracks share the highest R&B popularity score in the anniversary analysis.

2. **Account for Spotify-only coverage.** The results reflect the artists and releases in the dataset and how they perform on Spotify. Artists whose audiences are more active on other platforms may rank differently in a broader comparison. If the awards are intended to represent the wider music market, the committee could compare the Spotify shortlist with other streaming platforms or independent charts and check where the rankings differ.

3. **Use more listening data to refine the criteria.** The dataset contains popularity scores and follower counts, but it does not include monthly listeners, listening minutes, or detailed streaming history. If these metrics can be obtained, the committee could use them to distinguish **audience reach** (how many people listened), **engagement** (how much they listened), and **sustained interest** (whether listening held up over time). For example, Artist of the Year could consider unique listeners during the award year alongside follower count, while an anniversary award could consider how consistently a track attracted listeners over several years.

4. **Keep the three release windows and test the scoring weights.** Selecting one All-Time Favorite Track finalist from each window gives earlier releases a guaranteed place on the shortlist. Before confirming the winner, the committee should agree on how much each metric should count and publish the rule alongside the results.

5. **Check how much a single hit influences popularity-based scores.** This matters especially for the All-Time Favorite awards, where track popularity makes up 80% of the combined score. One standout track can make an artist look more popular across their catalogue than the available evidence supports, especially when only a few of their releases are in the dataset. We used median track popularity for All-Time Favorite Artist to reduce the influence of a single hit, but the result still depends on which tracks are included. For any award that uses popularity, we recommend checking the ranking against listening data over time. For artist awards, it would be important to check whether that interest extends across multiple releases.

## Repository Structure

```text
first_project/
├── data/
│   ├── raw/
│   │   ├── spotify_data_clean.csv      # Original Kaggle file
│   │   ├── track_data_final.csv        # Original Kaggle file
│   │   └── merged_spotify_data.csv     # Intermediate merge
│   └── clean/
│       ├── refined_dataset.csv         # Full cleaned dataset
│       ├── last_year_tracks.csv        # 2025 releases
│       ├── last_decade_tracks.csv      # 2015–2025 releases
│       └── other_2025.csv              # Genre mapping check for 2025 records with genre Other
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── awards_2025.ipynb
│   └── awards_last_decade.ipynb
├── sql_scripts/                        # Database creation, table population, analysis queries, and DrawDB diagram
└── README.md
```

## How to Run the Project
1. Clone the repository and open the `first_project/` folder.
2. Install pandas and JupyterLab with `python -m pip install pandas jupyterlab`, then start JupyterLab with `jupyter lab`.
3. Run all cells in `notebooks/data_cleaning.ipynb` to merge and clean the source data and generate the analysis CSVs.
4. Run `notebooks/awards_2025.ipynb` for the annual award rankings and `notebooks/awards_last_decade.ipynb` for the anniversary rankings.

## Database Setup and Workflow (MySQL Workbench)
1. **MySQL Configuration:** Ensure that `LOCAL INFILE` is enabled in your MySQL server and permitted by your MySQL Workbench connection before importing the data.
2. **Create the database:** Open MySQL Workbench and execute `sql_scripts/create_database.sql` to create the awards database and its tables.
3. **Populate the database:** Execute `sql_scripts/database_populate.sql` to import the CSV files into their corresponding tables. The script uses relative paths to locate the CSV files in the `sql_scripts/` folder. Follow the order of the import statements in the script to ensure that table dependencies and foreign key constraints are respected.
4. Check that the data has been successfully imported into all six tables using MySQL Workbench.