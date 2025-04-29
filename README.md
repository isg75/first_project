# �� Streaming Wars: Uncovering Content Strategies of Netflix and Prime Video

## �� Business Problem

With fierce competition in the streaming industry, data-driven decisions are crucial. 
Our team set out to uncover how content strategies differ between Netflix and Amazon Prime Video, focusing on content maturity, duration trends, and genre diversity.

**Hypotheses:**
- Amazon tends to push genre boundaries with more mature-rated content, while Netflix plays it safer with family-friendly options.
- Over the years, movies tend to be longer, and TV shows tend to be shorter.

We used data wrangling, EDA, and visual analysis to test and support these hypotheses.

---

## �� Dataset

- **Source:** Kaggle – Netflix and Amazon Prime Video datasets
- **Records:** Thousands of movies and TV shows
- **Features:** Title, platform, release year, type (movie/TV show), duration, rating, genres, and more.

---

## �� Data Cleaning & Preparation

Performed in Jupyter notebooks using Python (pandas):

- Removed duplicate records across both datasets.
- Fixed and standardized `release_year` inconsistencies.
- Unified genre and rating labels across platforms via custom dictionaries.
- Converted duration fields to numeric types for analysis.
- Designed a relational schema to handle many-to-many relationships between shows and genres.

---

## �� Database Structure

Implemented with relational integrity across combined Netflix and Prime datasets.

**Tables:**
- `shows (show_id, title, release_year, rating, duration, type, platform)`
- `genres (genre_id, genre_name)`
- `show_genres (show_id, genre_id)`

**ERD available in:** `charts/erd_diagram.png`

Relational integrity ensured via foreign key constraints.

---

## ��️ Technologies Used

- Python (pandas, seaborn, matplotlib)
- Jupyter Notebook
- Git + GitHub
- Google Slides (presentation)

---

## �� Exploratory Data Analysis & Visuals

EDA was conducted using bar charts, line plots, and percentage comparisons.

- TV shows are getting shorter over time, while movie durations remain stable.
- Netflix dominates the TV-MA category, whereas Prime has more family-friendly content.
- Drama is the leading genre for movies; Netflix offers more genre diversity in TV shows (documentary, sci-fi/fantasy, international).

We produced 5 high-quality visualizations that revealed key content strategies between platforms.

---

## �� Analytical Insights

Analysis performed via aggregations and filtering:

- Average movie duration over time by platform.
- Average number of TV show seasons over time by platform.
- Percentage of mature-rated content (TV-MA, R).
- Ratings distribution comparison between platforms.
- Top genres for movies and TV shows.

---

## �� Project Structure

```
project-root/
│
├── data/
│   ├── raw/
│   └── clean/
├── charts/                           # Graphs and visualizations, including ERD
├── notebooks/
│   └── netflix_cleaning.ipynb
│   └── prime_cleaning.ipynb
│   └── combined_analysis.ipynb
├── scripts/                          # Functions for cleaning and analysis
├── presentation_link.txt             # Google Slides link
├── README.md                         # This file
└── Trello_link.txt                   # Kanban board link
```

> This structure ensures reproducibility and separation of concerns between cleaning, analysis, and presentation.

---

## ✅ Rubric Alignment

- ✔️ Clear business problem + 2 hypotheses
- ✔️ Full data cleaning and justification
- ✔️ Functional relational structure with many-to-many handling
- ✔️ 5+ business questions answered with visual insights
- ✔️ 5+ visualizations with interpretation
- ✔️ Well-structured Git repo with daily commits
- ✔️ Comprehensive README for reproducibility
- ✔️ Google Slides presentation included

---

## �� Presentation Link

📽️ **[Google Slides – Final Presentation](https://docs.google.com/presentation/d/1LyJZ4CNOmA_cIpQm1TKKwAlBRQk3CE3RKp8zS3qdzhM/edit#slide=id.g34dd4655423_2_4517)**
