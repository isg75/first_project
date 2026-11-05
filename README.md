# Project overview
...

# Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/repository_name.git
```

2. **Install UV**

If you're a MacOS/Linux user type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a Windows user open an Anaconda Powershell Prompt and type :

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv 
```

3. **Activate the environment**

If you're a MacOS/Linux user type (if you're using a bash shell):

```bash
source ./venv/bin/activate
```

If you're a MacOS/Linux user type (if you're using a csh/tcsh shell):

```bash
source ./venv/bin/activate.csh
```

If you're a Windows user type:

```bash
.\venv\Scripts\activate
```

4. **Install dependencies**:

```bash
uv pip install -r requirements.txt
```

5. # Project Context

**Project:** Artist & music portfolio optimization strategy based on Spotify data

**Client / Role:** Senior management at a global record label or music agency (A&R – Artist and Repertoire division).

**Business Problem:** The label seeks to understand which factors (e.g., artist follower counts, song popularity, presence of explicit content) drive sustained global success. Decision-makers require data-driven guidance to determine which types of artists and song formats are worth investing in moving forward.
Identifying the ideal qualities of the next superstar(s)

**Outcome:** Proposal of 3 artist profiles / archetypes for future investments


6. # Questions 
Does artist popularity correlate with track popularity?
Does artist follower count relate to track popularity?
Do singles outperform track on albums?
Do certain genres outperform others?
Are up-and-coming artist worth analyzing?
Is there an optimal track length per genre?

7. ## Hypotheses
* Certain genres from past 10 years will be more popular than others and better for our artist profiles
* Singles performance better than albums in the past 10 years (bar chart)
* Artist with more followers have more popular tracks (scatter plot)
* Track popularity and artist popularity are largely correlated (scatter plot)


8. # Dataset 
* spotify_data clean.csv
* track_data_final.csv

9. ## Main dataset issues
* Two CSV files that appeared to be duplicates
* artist_genres missing from many artists
* Many genres and subgenres

10. ## Solutions for the dataset issues
* Comparative analysis between csv to determine unique data
    * Shape verification
    * Basic structure alignment (matching columns)
    * Data type comparison
    * Full content comparison (exact match check)
    * Bidirectional containment check (df1 vs. df2)
        * Result: spotify_data clean.csv is a subset of track_data_final.csv

* Artist_genres
    * Artist with genre data
        * Isolate artists with genre data and review genre
        * Classify into main_genres using key words
    * Artists missing genre data
        * Isolate artists with missing genre data
        * Group artists to determine number of unique artists and songs per artist
        * Enrich artist with 3 or more songs
        * Create a separate dataframe with enriched data to enrich original dataset

* Isolate "years" from "album_release_date" → Right(...., 4)

* Remove unnecessary columns
    * Explicit
    * track number

11. # EDA for Dataset
* Scatter plot
    * artist_followers vs track_popularity
    * artist_popularity vs track_popularity

* Line graph
    * genre and average artist popularity vs years
    * genre and song popularity vs years

* Tables
    * track type comparision: album, singles and compilation
    * track type comparison within genres: album, singles and compilation

12. ## Conclusions from EDA
    * Track popularity and artist popularity are largely correlated
    * Track popularity and artist followers are not always correlated
    * Albums on average support song popularity than singles
    * Artist who release albums have more followers than artist with singles
    * Generally, artist followers count grows rapidly when artist popularity is great than or equal to 40 and follower is between 300k and 500k 
    * Pop followed by hip-hop/rap are the most "popular" genres


13. # Project Recommendations
* Based on the data, we chose the three most consistent genres for durable artists and generated sonic profiles with Suno per our clients request.
    * Pop
    * Indie / Alternative
    * R&B / Soul
* Artist #1: NOVA - Pop Powerhouse
    * Genre: Pop
    * Best Format: Album + Singles before Albums
    * Hit length: 3 min 23 seconds
    * Sound Signature: Soulful yet danceable. Embodies love, belonging, and courage. Exceptional as a solo act or with a full band.
    * Sonic sample: https://suno.com/s/YUhA1dFDSDKPbcH5   
* Artist #2: Ellis Vance - Indie singer/songwriter
    * Genre: Indie / Alternative
    * Best Format: Album
    * Hit length: 3 min 36 seconds
    * Sound Signature: Conversational vocals, gentle wavy guitars, warm bass, synths. Written like a diary with a catchy chorus. If it’s not stuck in your head, it’s not his song.
    * Sonic sample: https://suno.com/s/OhPwVg9VbECSNcsh
* Artist #3: Sable Bank
    * Genre: R&B / Soul
    * Best Format: Album
    * Hit Length: 3 minutes 25 seconds
    * Sound Signature: Soft vocals over deep bass  and hazy synths. Intimate verses open into lush harmonies. Edgy and mildly misbehaved.
    * Sonic sample: https://suno.com/s/hfawD5JlxDbbIWXx


14. # Next steps

* Artist Profile Testing - Audio Features & Sonic Profiling
    * Begin sampling AI created songs with groups to build “sonic profiles” and “build the next new artist”.

* Structural Data Enrichment (Unique IDs & subgenre hierarchy):
    * Build a more sophisticated data structure to track artists with unique IDs and subgenres + MORE DATA.

* Predictive Modeling (Machine learning for track popularity forecasting).
    * Develop machine learning models to forecast the potential popularity score of unreleased songs ( based on: track features, historical artist performance, and album release formats)

* External Data Integration (Social media early detection).
    * Integrate social media metrics and external streaming signals (e.g., TikTok trends, Instagram engagement rates, Shazam charts) to identify fast-growing, up-and-coming artists before mainstream Spotify metrics reflect their growth.
