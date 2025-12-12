# 🏙️ Berlin Urban Safety Analysis: A BIUS Project

---

## Project Overview

The Berlin Institute for Urban Safety (BIUS) is an independent, non-profit think tank dedicated to researching the causes and consequences of crime for evidence-based policy recommendations.

This project is an independent analysis conducted on behalf of BIUS, aiming to investigate crime patterns in Berlin by combining demographic and crime datasets.

The presentation is available [here](https://docs.google.com/presentation/d/1Y4ldaEibWwJ1H7KI63VCK8tHZ-8zNZeO/edit?usp=sharing&ouid=105239850282776443277&rtpof=true&sd=true).
---

## 💾 Data Sources

The analysis merges two key public datasets, linked by geographic identifiers (postal/area codes and districts):

| Dataset                        | Source                                                    | Purpose                                                                                    |
| :----------------------------- | :-------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| **Crimes in Berlin**           | Kaggle: `martincymorek/berlin-crimes`                     | Core data for all crime counts by year and area.                                           |
| **Berlin District Population** | Kaggle: `shreejahoskerenatesh/berlin-district-population` | Provides population counts by age group and gender for calculating per-capita crime rates. |

---

## Day 1: Exploration and Hypothesis Formulation

The initial day focused on exploratory data analysis (EDA) and defining the analytical framework.

### Analysis Goals

1. **Goal A:** Develop a Crime Risk Index — a weighted index that combines crime rates (crime count / population) to rank districts.
2. **Goal B:** Identify correlations between demographics and crime — check whether specific age groups are associated with certain crime types.
3. **Goal C:** Analyze crime specialization and temporal trends — investigate unique crime patterns in districts and changes over time.

### Testable Hypotheses

| ID     | Category                  | Hypothesis Statement                                                                                                                |
| :----- | :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| **H1** | General Crime Rate        | Districts with higher population density will have a higher absolute number of non-violent crimes.                                  |
| **H2** | General Crime Rate        | The **Regierungsviertel** will have an above-average rate of **Threat** and **Damage** (per capita).                                |
| **H3** | Demographics (Age)        | Locations with a higher proportion of residents aged **65 and older** will show a higher rate of **Burglary** per capita.           |
| **H4** | Demographics (Age)        | Locations with a higher proportion of the **18-27** age group will correlate with a higher rate of **Drugs** offenses (per capita). |
| **H5** | Specific Crime (Temporal) | The rate of **Car theft** has declined over the years covered in the dataset.                                                       |

---

## Day 2: Data Cleaning and Preprocessing

The second day focused on preparing the raw data for analysis and ensuring consistent formatting.

### Key Cleaning Steps (Python/Pandas)

1. **Column Name Standardization:** Translated and standardized column names (e.g., spaces replaced with underscores).
2. **Umlaut Removal:** Removed special characters from string columns to avoid encoding issues.
3. **Initial EDA:** Conducted preliminary analysis to check distributions, missing values, and data quality.

---

## Day 3: Data Integration, Feature Engineering, and MySQL Queries

Day 3 focused on merging the datasets, calculating features, and creating SQL queries for analysis.

### Data Integration and Modeling (ERD)

For this project, we have **three main tables**:

### 1. `population_data`

Contains demographic information per postal code.

**Key columns:**

- `postal_code` → unique identifier for each postal code
- `district` → Berlin district name
- `total` → total population
- Age group columns: `age_under_6`, `age_6_to_15`, `age_15_to_18`, `age_18_to_27`, `age_27_to_45`, `age_45_to_55`, `age_55_to_65`, `age_65_plus`
- `female_total` → total female population

---

### 2. `location_bridge`

Maps districts to postal codes and specific locations.

**Key columns:**

- `district` → district name
- `code` → postal/area code
- `location` → specific location/neighborhood within the district

---

### 3. `crime_data`

Contains crime counts by location and year.

**Key columns:**

- `year` → year of record
- `district` → district name
- `code` → postal/area code
- `location` → location name
- Multiple crime type columns: `robbery`, `street_robbery`, `injury`, `agg_assault`, `threat`, `theft`, `car`, `from_car`, `bike`, `burglary`, `fire`, `arson`, `damage`, `graffiti`, `drugs`, `local`

---

### 🔗 Relationships

- **`population_data` → `location_bridge`**:  
  Linked via `district` and optionally `postal_code`. Allows mapping demographic data to specific locations.

- **`location_bridge` → `crime_data`**:  
  Linked via `district`, `code`, and `location`. Provides aggregation of crime counts per district or location.

- **`population_data` → `crime_data`**:  
  Can be joined through `district` and `postal_code` (via the bridge if needed) to calculate per-capita crime rates and demographic correlations.

---

## Crime Analysis – Hypotheses Testing in MySQL

In this project, we tested several hypotheses related to crime patterns across Berlin districts using MySQL. We calculated normalized crime metrics based on population and age groups.

### H1 – Overall Threat & Damage

- Calculated threat level per every 1000 residents for each district.
- **Finding:** Tempelhof-Schöneberg, Mitte, and Friedrichshain-Kreuzberg have the highest threat per 1,000 residents, while Treptow-Köpenick, Lichtenberg, and Pankow have the lowest.
- **Conclusion:** Certain central districts experience disproportionately higher threats relative to population.

### H3 – Older Population & Burglary

- Analyzed burglary incidents relative to the older population.
- **Finding:** Mitte and Tempelhof-Schöneberg show higher burglary incidents per older resident, whereas districts like Treptow-Köpenick and Lichtenberg have lower rates.
- **Conclusion:** Burglary risk is concentrated in more central districts with higher older population density.

### H4 – Young Population & Drug Offenses

- Calculated drug-related crimes relative to the young population.
- **Finding:** Mitte, Friedrichshain-Kreuzberg, and Tempelhof-Schöneberg show the highest incidence per young resident; Treptow-Köpenick and Lichtenberg are lowest.
- **Conclusion:** Drug offenses are more prevalent in central districts with higher young population density.

### H5 – Car Theft Trend Over Years

- Aggregated total car thefts from 2012–2019.
- **Finding:** Steady increase until 2016 (peak: 7,784 thefts), followed by a decline to ~6,138 in 2019.
- **Conclusion:** Car theft trends indicate a peak period followed by stabilization, suggesting impact of preventive measures or enforcement policies.

**Overall:**  
Our MySQL queries enabled normalization of crime data relative to population and age groups, confirming that central districts face higher crime rates, while trends like car theft vary over time. These insights validate our initial hypotheses and provide a basis for targeted interventions.

---

### Presentation

The following slides will visualize key findings, supported by MySQL queries and data analysis performed during the project.

> https://docs.google.com/presentation/d/1Y4ldaEibWwJ1H7KI63VCK8tHZ-8zNZeO/edit?usp=sharing&ouid=105239850282776443277&rtpof=true&sd=true
