# Green Light Analytics: What Film Should We Greenlight Next?

## Team Members

- Catarina
- Bindu Valmiki

## Introduction

Green Light Analytics helps film studios decide which movies to "greenlight", meaning approve for production. In this project, a small film studio planning a US cinema release asked us one question: **what kind of film should we make next to be both well rated and commercially successful?**

To answer it, we analysed the IMDb Top 1000 dataset: the 1000 highest-rated films on IMDb, with their genre, release year, runtime, age certificate, audience rating, critic score (Meta_score), number of votes, director, lead actors and US box office (Gross). We cleaned the data, explored it to answer six business questions, and turned the findings into recommendations for the studio.

## Business Questions

The client's business questions:

1. **Genres:** Which genres produce the most top-rated films, and which earn the most at the box office?
2. **Rating vs. box office:** Does a high rating mean high box office, or does popularity (number of votes) matter more?
3. **Critics vs. audiences:** Do critics (Meta_score) and audiences (IMDb rating) agree on what makes a great film?
4. **Talent:** Which directors and actors consistently deliver highly rated and profitable films?
5. **Trends over time:** How has the mix of top films changed over the decades, and which genres are rising?
6. **Age certificate:** Does a film's age rating affect how much it earns?

## Dataset

- **Source:** [IMDB Movies Dataset – Top 1000 Movies and TV Shows (Kaggle)](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
- **Licence:** _[check on the Kaggle page and add]_
- **Size:** 1,000 movies, 16 columns
- **Main variables:** title, release year, certificate, runtime, genre, IMDb rating, Meta score, director, four main stars, number of votes and gross revenue

### Limitations

- The dataset contains only the top 1000 rated films, so it shows what successful films have in common, not why films fail.
- Gross covers US box office only, not streaming or international revenue, and is not adjusted for inflation.
- The data ends around 2020.

### Main dataset issues

- `released_year` stored as text, with one invalid value ("PG" for Apollo 13)
- `runtime` stored as text with units ("142 min")
- Titles are not unique ("Drishyam" appears twice)
- Missing values in `certificate`, `meta_score` and `gross`
- `gross` stored as text with commas

### Solutions for the dataset issues

- Standardised column names to lowercase snake_case
- Removed `poster_link` and `overview`, as they are not needed for the analysis
- Corrected Apollo 13's release year to 1995 (verified on IMDb) and converted `released_year` to integer
- Removed " min" from `runtime` and converted it to integer
- Checked "Drishyam": two different films (2013 original and 2015 remake), both kept
- Added `movie_id` as a unique identifier, since titles are not unique
- Checked text columns for extra spaces and broken characters
- Missing values in `certificate`, `meta_score` and `gross`: _[to be completed]_

## Database Design

_[Describe the main entities, the relationships between them and the reasoning behind the design.]_

![Entity-Relationship Diagram](images/erd.png)

## SQL Analysis

_[Most relevant queries and results.]_

## Python Analysis

_[Main findings from the exploratory analysis, with selected charts.]_

## Key Findings

_[Main conclusions, each supported by evidence from the data.]_

## Business Recommendations

_[Specific, realistic actions for the studio based on the findings.]_

## Repository Structure

```
project-name/
├── data/
│   ├── raw/            # original dataset
│   └── processed/      # cleaned datasets and table files
├── notebooks/          # data cleaning, table preparation, EDA, visualisations
├── sql/
│   ├── schema.sql      # creates the database tables
│   ├── load_data.sql   # loads the processed data
│   └── queries.sql     # business question queries
├── images/             # ERD and charts
├── presentation/       # final presentation
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/catarina-bm/first_project.git
cd first_project
```

2. **Install UV**

If you're a macOS/Linux user, type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a Windows user, open an Anaconda PowerShell Prompt and type:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv
```

4. **Activate the environment**

If you're a macOS/Linux user (bash shell), type:

```bash
source ./.venv/bin/activate
```

If you're a macOS/Linux user (csh/tcsh shell), type:

```bash
source ./.venv/bin/activate.csh
```

If you're a Windows user, type:

```bash
.\.venv\Scripts\activate
```

5. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

## How to Run the Project

1. Launch JupyterLab from the terminal (with the environment activated) and select the venv kernel:

```bash
python -m jupyter lab
```

2. Run the notebooks in order (01 → 04).
3. Run `sql/schema.sql` to create the database.
4. Run `sql/load_data.sql` to load the processed data.
5. Run `sql/queries.sql` to reproduce the analysis.

## Next Steps

_[Ideas to extend the analysis.]_
