# NYC Jobs Data Analysis & Data Cleaning Project

## Overview

This project focuses on cleaning, transforming, and analyzing public job postings for New York City, using a structured Python (Pandas) workflow and custom functions for robust data wrangling. The source data includes large CSVs with diverse job roles, salary ranges, and categorical features. The main goal is to provide clean, analysis-ready datasets for insights into salary distributions, contract types, agency trends, and demand for data-centric skills.

The project is organized into modular Jupyter notebooks and Python scripts, with a special emphasis on reproducible preprocessing and targeted extraction of roles related to data analysis, engineering, and modern data skills.

The workflow is structured around dynamic file paths managed via a YAML configuration file, ensuring portability and easy customization.

---

## Data Sources

- **NYC Jobs CSV files:** Two separate CSVs with thousands of job postings, each containing up to 30 columns.
- **YAML configuration:** Manages all input/output paths for raw and cleaned data, as well as output figures.

---

## Main Files and Structure

### 1. `data_wrangling.ipynb`

- Loads raw CSVs and YAML config for path management.
- Applies cleaning functions from `functions.py`:
  - Standardizes column names.
  - Drops duplicates by job ID.
  - Removes unnecessary columns.
  - Cleans punctuation and normalizes text (job titles, skills).
  - Converts dates to pandas datetime format.
- Filters jobs by:
  - **Business title** (extracts roles like "data analyst", "data engineer").
  - **Preferred skills** (finds mentions of SQL, Python, BI, Tableau, ML, etc.).
- Outputs three grouped CSVs:
  - All other jobs.
  - Data analyst/engineer roles.
  - Jobs requiring specific data skills.
- Includes summary tables for nulls, column types, and value counts.

### 2. `functions.py`

- Contains all custom data cleaning and transformation functions:
  - Standardize column names.
  - Drop duplicates.
  - Concatenate DataFrames.
  - Remove punctuation and lowercase.
  - Drop irrelevant columns.
  - Regex-based row filtering.
  - Standardize dates.
- Functions are written for flexible, repeatable use in notebooks.

### 3. `data_insights - Copy.ipynb`

- Loads cleaned CSVs and applies further transformation as needed.
- Explores:
  - Salary distributions by role type and skill requirements.
  - Contract frequency (annual, hourly, daily) by group.
  - Posting trends over time, highlighting recent demand for data talent.
- Produces visualizations (matplotlib, seaborn):
  - KDE plots for salary bands.
  - Bar charts for contract types and agency hiring.
  - Histograms for posting year.
- Includes documented code cells explaining each plot and table and how to interpret results.

---

## Configuration

- All file paths for raw inputs, cleaned outputs, and figures are managed in `config.yaml`:
  - Update this file to change inputs and outputs without modifying notebook logic.
  - Example outputs managed via YAML include:
    - Cleaned CSVs by job type and skill.
    - Figures for salary, agency, and trends.

---

## Key Features

- **Robust Data Cleaning:** Handles missing values, inconsistent text, irrelevant columns, and duplicates.
- **Skill Filtering:** Extracts jobs by business title and by presence of data-related keywords in the skills field using regex.
- **Date Normalization:** Converts multiple date formats to pandas datetime for time-series analysis.
- **Modular Outputs:** Splits the cleaned data into logical groups for focused analysis.
- **Configurable Workflow:** Uses YAML for paths, making the notebooks portable and reusable.

---

## Example Insights

- **Salary Distribution:** Data analyst and engineering roles have higher median starting salaries compared to general postings. Jobs mentioning modern data skills also tend to offer higher pay.
- **Contract Type:** Most data-related roles are annual contracts; hourly/daily contracts are rare.
- **Trends Over Time:** Demand for data-centric jobs is increasing, with more postings in recent years.
- **Agency Hiring:** Top agencies hiring for data roles can be visualized and ranked using the included analysis

---

## How to Use

1. **Configure file paths:** Update `config.yaml` as needed for input/output CSVs and figures.
2. **Run `data_wrangling.ipynb`:** This notebook processes raw data into analysis-ready CSVs.
3. **Run `data_insights.ipynb`:** Explore cleaned datasets and generate summary tables and visualizations.
4. **Customize filtering:** Adjust regex patterns or column selections in notebooks/scripts to focus on different roles or skills if needed.

---

## Files Included

- `data_wrangling.ipynb` — Main notebook for data cleaning and preparation.
- `functions.py` — Library of custom preprocessing functions.
- `data_insights.ipynb` — Notebook for data analysis and visualization.
- `config.yaml` — Centralized config for all input/output file locations.
- **CSV Outputs:** Cleaned, grouped datasets for further analysis (paths managed with YAML).
- **Figures:** Visual outputs saved per YAML config.

## Presentation Slides
[[Link to Slides](https://www.canva.com/design/DAG0Ra3GTHo/xIG_axW6IWI_54hR0ECAoQ/edit?utm_content=DAG0Ra3GTHo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)]

---

## Authors
- Janna Julian
- Sina Yazdi
- Luis Pablo Aiello

---

## License

This repository is for educational, analytical, and non-commercial purposes only. Data is derived from publicly available NYC jobs datasets.