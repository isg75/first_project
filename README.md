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

Business case
(Recommended) Business Case: Artist &Repertoire and Music Portfolio Optimization Strategy
Client / Role: Senior management at a global record label or music agency (A&R – Artist and Repertoire division).

Business Problem: The label seeks to understand which factors (e.g., artist follower counts, song popularity, presence of explicit content) drive sustained global success. Decision-makers require data-driven guidance to determine which types of artists and song formats are worth investing in moving forward.
Identifying the ideal qualities of the next superstar(s)

* 3 Ideal Superstar Profiles

Hypotheses:

* Certain genres from past 10 years will be more popular than others and better for our artist profiles
* Singles performance better than albums in the past 10 years (bar chart)
* Artist with more followers have more popular tracks (scatter plot)
* Track popularity and artist popularity are largely correlated (scatter plot)



DATA CLEANING:

* Are the Excels the same data? Or different data? 
    * Columns, names, contents, and data types
    * Merge tables
* Clean up the data in the "cleaned" 
    * isolate "years" from "album_release_date" → Right(...., 4)
    * artist_genres
        * try to enrich and cluster into high_level_genres
        * Charles enriched ~2000 songs_id with artist_genre
        * Gebra sorted roughly ~4000 with parsing
        * Total should be roughly ~6000 songs with genres for analysis
    * remove columns
        * Explicit
        * track number


EDA:

    * Categorical
        * album_type - DEEP DIVE to understand statistics and distribution of song-popularity
            * Single
            * Album
            * Compilation
        * artist_genre - use current data
            * standard statistics, averages, describe
            * song popularity
        * Describe (Numerical)
            * Duration - We'll focus on this once we define genres of artists
            * Artist Popularity - We'll focus on this for touring together
            * Year - 


#Business case
(Recommended) Business Case: Artist &Repertoire and Music Portfolio Optimization Strategy
Client / Role: Senior management at a global record label or music agency (A&R – Artist and Repertoire division).

#Business Problem: 
The label seeks to understand which factors (e.g., artist follower counts, song popularity, presence of explicit content) drive sustained global success. Decision-makers require data-driven guidance to determine which types of artists and song formats are worth investing in moving forward.
Identifying the ideal qualities of the next superstar(s)

#OUTCOME
3 Ideal Superstar Profiles


DATA CLEANING:




#EDA:

    * Categorical
        * album_type - DEEP DIVE to understand statistics and distribution of song-popularity
            * Single
            * Album
            * Compilation
        * artist_genre - use current data
            * standard statistics, averages, describe
            * song popularity
        * Describe (Numerical)
            * Duration - We'll focus on this once we define genres of artists
            * Artist Popularity - We'll focus on this for touring together
            * Year - 



#FOCUS TOMORROW AND DISCUSS TO REFINE

#INSIGHTS FROM DAY 1

* Artist with more followers have more popular tracks (scatter plot)
* Track popularity and artist popularity are largely correlated (scatter plot)
* Albums generally support song popularity than singles
* Artist who release albums have more followers than artist with singles
* Generally, at are will experience the fastest growth once popularity is >= 40 (roughly)
* Pop followed by hip-hop/rap are the most "popular" genres


#WORK TO BE DONE

* DBDraw between:
    * artist-genre dictionary
    * cleaned spotify data (filtered for past 10 years)
* We need to make a bridge table combining these two tables with our final results


DEFINE OUR FUTURE SUPERSTAR ARCHETYPE

* Artist popularity: 35 to 65
* Top 3 genres
* Singles vs albums per genre
* Optimal track length
* Similar artists to tour with



# Questions 
Does artist popularity correlate with track popularity?
Does artist follower count relate to track popularity?
Do singles outperform album tracks?
Do certain genres outperform others?
Is there an optimal track length per genre?

# Proposal to answer questions
* Certain genres from past 10 years will be more popular than others and better for our artist profiles -> Group by
* Singles performance better than albums in the past 10 years -> bar chart
* Artist with more followers have more popular tracks -> scatter plot
* Track popularity and artist popularity are largely correlated -> scatter plot

# Dataset 
...

## Main dataset issues
* Two datasets that are likely duplicates
* Certain columns unnecessary
* Dates should be only years
* 

## Solutions for the dataset issues
* Are the Excels the same data? Or different data? 
    * Columns, names, contents, and data types
    * Merge tables
* Clean up the data in the "cleaned" 
    * isolate "years" from "album_release_date" → Right(...., 4)
    * artist_genres
        * try to enrich and cluster into high_level_genres
        * Charles enriched ~2000 songs_id with artist_genre
        * Gebra sorted roughly ~4000 with parsing
        * Total should be roughly ~6000 songs with genres for analysis
    * remove columns
        * Explicit
        * track number

# Conclussions
...

# Next steps
...
