# From Poor Ratings to Exceptional Stays

## A Data Driven Analysis of Factors Influencing Airbnb Guest Satisfaction

This project analyzes Airbnb property listings to identify factors associated with property prices and guest ratings, with particular attention to poorly rated listings.

The main business problem is:

> **What factors contribute to lower Airbnb guest ratings, and what improvements can hosts prioritize to improve poorly rated listings?**

The project combines Python and MySQL within one analytics workflow. Python and Pandas were used for data loading, cleaning, transformation, feature engineering, exploratory data analysis, statistical testing, and visualization. MySQL was used to store the cleaned dataset and perform structured queries, filtering, grouping, and aggregation.

## Team

| Team Member | Role |
| --- | --- |
| Jan Noel Vero | Program Manager |
| Nadiya | Member |

## Goal and Objective

### Goal

Identify the characteristics of low rated Airbnb listings and determine which property features are associated with higher guest satisfaction.

### Objective

Analyze Airbnb listing characteristics that influence guest ratings and identify practical strategies for improving underperforming listings.

## Project Workflow

```text
Raw Airbnb Data
        ↓
Python Data Loading
        ↓
Data Validation
        ↓
Missing Value Analysis
        ↓
Duplicate Detection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Clean Dataset
        ↓
Python EDA               MySQL Database
        ↓                       ↓
Statistical Tests          SQL Analysis
        ↓                       ↓
        └──────────┬────────────┘
                   ↓
             Visualizations
                   ↓
              Key Findings
                   ↓
            Recommendations
```

Python and SQL were used as complementary analytical tools. Python supported data preparation, statistical testing, and visualization, while SQL supported structured storage, filtering, grouping, aggregation, and analytical querying.

## Research Questions

### RQ1

What is the distribution of Airbnb listings based on high, average, and low ratings?

### RQ2

Is there a significant difference in price between poorly rated and highly rated Airbnb listings?

### RQ3

Which property types are more likely to receive poor guest ratings?

### RQ4

Do amenities significantly influence the price of Airbnb listings?

### RQ5

Do amenities significantly influence Airbnb ratings?

### RQ6

Does the location of an Airbnb listing significantly influence guest ratings?

### RQ7

Does the location of an Airbnb listing significantly influence Airbnb prices?

### RQ8

Does the number of reviews significantly influence Airbnb ratings?

### RQ9

Which month is associated with the highest aggregated review count and the highest average Airbnb rating in the dataset?

### RQ10

What improvements should Airbnb hosts prioritize to transform poorly rated listings into highly rated accommodations?

## Dataset

The project uses Airbnb property listing data containing information about property characteristics, listing descriptions, location, price, guest ratings, reviews, and amenities.

Following cleaning and feature engineering, the final dataset contains:

| Dataset Metric | Final Result |
| --- | ---: |
| Airbnb listings | 604 |
| Variables | 24 |

The cleaned dataset is exported as:

```text
airbnb_cleaned.csv
```

### Final Variables

```text
Property Name
Listing Description
Property Type
City
Country
Month
Price(in dollar)
Rating
Number of Reviews
Rating Rank
Price Rank
WiFi
Pool
Sauna
Hot Tub
Fireplace
Wood Stove
Parking
Kitchen
Beach
Waterfront
Sea View
Mountain View
Amenity Count
```

## Data Cleaning and Preparation

The original Airbnb data required cleaning and transformation before reliable analysis could be performed.

### Main Dataset Issues

1. Missing values, particularly in ratings
2. Duplicate listing records
3. Price information that required conversion to numeric values
4. Rating information that required cleaning and standardization
5. Review information that required extraction and conversion
6. Property and location information that required restructuring
7. Date information that required conversion into month
8. Property names containing invalid special character patterns
9. Amenities embedded within listing descriptions
10. Structural differences across the source datasets

### Cleaning Process

Python and Pandas were used for the main data preparation process.

Initial inspection included dataset dimensions, column names, data types, missing values, duplicate records, unique values, and descriptive statistics.

Missing ratings were identified and handled during cleaning. Duplicate records were inspected and removed, followed by a final duplicate check.

Property information was cleaned and standardized. Listings with invalid property name patterns were removed where necessary.

Location information was restructured into:

```text
City
Country
```

Date information was transformed into a standardized `Month` variable.

Price was cleaned and converted into numeric format using:

```text
Price(in dollar)
```

Rating information was cleaned and converted into numeric format.

### Rating Categories

| Rating Category | Definition |
| --- | --- |
| Low Rating | Below 4.5 |
| Average Rating | 4.5 to below 4.8 |
| High Rating | 4.8 or above |

The number of reviews was extracted and stored as `Number of Reviews`.

## Feature Engineering

Additional variables were created to support the analysis:

```text
Rating Rank
Price Rank
Amenity Count
```

Individual amenity indicators were extracted from listing descriptions:

```text
WiFi
Pool
Sauna
Hot Tub
Fireplace
Wood Stove
Parking
Kitchen
Beach
Waterfront
Sea View
Mountain View
```

Each amenity variable indicates whether that amenity was detected in the listing information. `Amenity Count` represents the number of identified amenities associated with each listing.

## MySQL Integration

The cleaned Pandas DataFrame was transferred into MySQL using SQLAlchemy and PyMySQL.

Database:

```sql
airbnb_project
```

Main table:

```sql
airbnb_listings
```

SQL was used for filtering, grouping, aggregation, property comparisons, location comparisons, rating analysis, price analysis, review analysis, and amenity analysis.

## Exploratory Data Analysis

Exploratory data analysis was conducted using Python and SQL.

The analysis examined:

1. Dataset structure
2. Rating distribution
3. Price distribution
4. Property types
5. Countries and cities
6. Guest ratings
7. Number of reviews
8. Amenities
9. Monthly patterns
10. Relationships between analytical variables

## Statistical Methodology

Inferential statistical methods were used to evaluate whether observed relationships and differences were statistically significant.

### Mann Whitney U Test

Used to compare prices between poorly rated and highly rated Airbnb listings.

### Spearman Correlation

Used to examine relationships between:

1. Amenity Count and Price
2. Amenity Count and Rating
3. Number of Reviews and Rating

### Kruskal Wallis Test

Used to evaluate differences in:

1. Ratings across locations
2. Prices across locations

These nonparametric methods were used to examine relationships and group differences without relying on normal distribution assumptions.

# Key Findings

## RQ1: Rating Distribution

The majority of properties in the dataset are highly rated.

| Rating Category | Listings | Percentage |
| --- | ---: | ---: |
| High | 460 | 76.16% |
| Average | 124 | 20.53% |
| Low | 20 | 3.31% |

Only 20 listings are classified as poorly rated. Because this group represents a small proportion of the dataset, comparisons involving low rated properties should be interpreted cautiously.

## RQ2: Price and Rating

Highly rated listings were more expensive than poorly rated listings.

| Metric | Poorly Rated | Highly Rated |
| --- | ---: | ---: |
| Average Price | $102.55 | $168.93 |
| Median Price | $79 | $131 |

The Mann Whitney U test produced:

| Statistic | Result |
| --- | ---: |
| U Statistic | 2939.5 |
| P Value | 0.0063 |

The difference is statistically significant at the 0.05 significance level. Listing price is therefore significantly associated with rating category in this dataset.

## RQ3: Property Type and Poor Ratings

Hotel rooms and hotels recorded the highest proportion of poorly rated listings at 16.67 percent, followed by lofts at 15.38 percent.

Apartments had a lower poor rating proportion of 9.33 percent but contributed the greatest number of poorly rated listings overall, with seven properties.

Hotels and hotel rooms each contain only six listings, meaning their 16.67 percent rate represents one poorly rated property in each category. Results for property types with small sample sizes should therefore be interpreted cautiously.

## RQ4: Amenities and Price

The relationship between amenity count and Airbnb price produced:

| Statistic | Result |
| --- | ---: |
| Spearman Correlation | 0.101 |
| P Value | 0.013 |

The relationship is statistically significant but weak.

| Amenities Mentioned | Listings | Average Price | Median Price |
| ---: | ---: | ---: | ---: |
| 0 | 409 | $144.04 | $112.00 |
| 1 | 159 | $188.80 | $131.00 |
| 2 | 28 | $195.25 | $154.50 |
| 3 | 8 | $224.75 | $130.00 |

Average price generally rises as more amenities are mentioned, but median prices do not increase consistently. Amenity count alone is therefore not a strong determinant of price.

## RQ5: Amenities and Guest Ratings

The relationship between amenity count and Airbnb rating produced:

| Statistic | Result |
| --- | ---: |
| Spearman Correlation | -0.115 |
| P Value | 0.0045 |

The relationship is statistically significant but very weak and negative.

| Amenities Mentioned | Listings | Average Rating | Median Rating |
| ---: | ---: | ---: | ---: |
| 0 | 409 | 4.858 | 4.890 |
| 1 | 159 | 4.827 | 4.860 |
| 2 | 28 | 4.830 | 4.855 |
| 3 | 8 | 4.802 | 4.830 |

The number of amenities mentioned is not a strong driver of guest satisfaction. More amenities do not necessarily correspond with better guest ratings.

## RQ6: Location and Rating

Guest ratings differed significantly across locations.

| Statistic | Result |
| --- | ---: |
| Kruskal Wallis H | 74.730 |
| P Value | Below 0.001 |

Selected average ratings included:

| Location | Average Rating |
| --- | ---: |
| North Carolina, US | 4.963 |
| United Kingdom | 4.927 |
| Germany | 4.925 |
| Malaysia | 4.747 |
| Vietnam | 4.756 |
| Spain | 4.762 |

Location is significantly associated with guest ratings in this dataset. The test establishes that at least one location differs from another, but it does not establish that location causes the observed rating differences.

## RQ7: Location and Price

Airbnb prices differed significantly across locations.

| Statistic | Result |
| --- | ---: |
| Kruskal Wallis H | 175.778 |
| P Value | 4.68 × 10⁻²⁵ |

Selected average prices included:

| Location | Average Price |
| --- | ---: |
| California, US | $371.91 |
| Texas, US | $264.60 |
| North Carolina, US | $235.83 |
| Germany | $79.38 |
| Vietnam | $66.62 |
| Malaysia | $56.70 |

The findings show that geographic market differences are an important factor in Airbnb pricing.

## RQ8: Number of Reviews and Rating

The relationship between review count and guest rating produced:

| Statistic | Result |
| --- | ---: |
| Spearman Correlation | -0.184 |
| P Value | 5.38 × 10⁻⁶ |

The relationship is statistically significant but weak. Listings with more reviews tend to have slightly lower ratings in this dataset.

This result does not demonstrate that receiving more reviews causes ratings to decline.

## RQ9: Month, Reviews, and Rating

Listings associated with June had the highest aggregated `Number of Reviews` value at 66,386.

May recorded the highest average rating at 4.98, but May contains only one listing.

The monthly distribution is highly uneven:

1. June contains 401 of the 604 listings
2. January contains one listing
3. May contains one listing
4. December contains two listings

This result requires careful interpretation. `Number of Reviews` represents the review count associated with each listing and does not establish that those reviews were written during the month assigned to the listing.

Therefore, the June result should be interpreted as the highest aggregated review count among listings associated with June, not as evidence that June had the highest monthly review activity or represented peak travel season.

## RQ10: Improving Poorly Rated Listings

The combined findings indicate that hosts should prioritize the overall guest experience rather than simply increasing the number of amenities.

The analysis supports four main areas of improvement:

### Service Quality

Prioritize cleanliness, property condition, service consistency, and accurate listing descriptions.

### Guest Expectations

Set realistic expectations and ensure that the actual stay matches what is promised in the listing.

### Smart Pricing

Position and price the property competitively relative to its local market and property type.

### Amenity Quality

Provide useful, functional, relevant, and well maintained amenities. Quantity alone does not improve guest ratings.

# Business Recommendations

## Prioritize Guest Experience

Focus on the quality and consistency of the stay, particularly cleanliness, property condition, service quality, and accuracy of listing information.

## Ensure Value for Money

The quality of the accommodation and overall guest experience should justify the listing price.

## Benchmark Locally

Compare the property with similar listings in the same geographic market and property type when setting prices and positioning the listing.

## Curate Useful Amenities

Focus on functional and relevant amenities that improve the guest experience rather than increasing the number of amenities simply for marketing purposes.

## Monitor Guest Feedback

Track recurring complaints and guest comments to identify specific operational issues requiring attention.

# Limitations

## Rating Group Imbalance

Only 20 of the 604 listings were classified as poorly rated. The relatively small low rating group limits the strength of comparisons involving underperforming properties.

## Property Type Sample Sizes

Some property types have very small numbers of listings. For example, hotels and hotel rooms each contain only six listings. Percentage comparisons for these categories should therefore be interpreted cautiously.

## Geographic Imbalance

The number of listings varies considerably across locations, so results for geographic groups with smaller samples should be interpreted carefully.

## Monthly Imbalance

June contains 401 of the 604 listings, while January and May contain only one listing each and December contains only two.

## Review Data Limitation

`Number of Reviews` represents the review count associated with a listing and does not necessarily represent reviews submitted during the listing's associated month. Monthly review totals should therefore not be interpreted as actual review activity occurring within each month.

## Association Does Not Establish Causation

The statistical analyses identify associations and differences within the dataset. They do not establish that price, location, amenities, property type, or review volume directly cause higher or lower ratings.

# Next Steps

Future analysis could strengthen the project by:

1. Expanding the dataset to include more poorly rated listings
2. Improving geographic balance across locations
3. Collecting review level data with individual review dates
4. Analyzing individual amenities rather than only total amenity count
5. Adding variables such as bedrooms, bathrooms, guest capacity, property size, neighborhood, host experience, host response rate, cleaning quality, cancellation policy, and length of stay
6. Conducting multivariable regression analysis
7. Conducting post hoc testing after significant Kruskal Wallis results
8. Developing a predictive model to identify listings at greater risk of receiving poor ratings

# Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Data analysis and statistical workflow |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| MySQL | Relational database and SQL analysis |
| SQL | Structured querying |
| SQLAlchemy | Python and MySQL integration |
| PyMySQL | MySQL database connectivity |
| SciPy | Statistical testing |
| Matplotlib | Data visualization |
| Seaborn | Data visualization |
| Jupyter Notebook | Interactive analysis |
| Git | Version control |
| GitHub | Collaboration and repository management |
| UV | Python environment and dependency management |

# Repository Structure

```text
first_project/
│
├── data/
├── figures/
├── notebooks/
├── slides/
├── sql_scripts/
├── src/
├── config.yaml
├── pyproject.toml
├── uv.lock
└── README.md
```

### `data`

Contains project datasets, including the cleaned dataset used for analysis.

### `figures`

Contains charts and visualizations generated during the analysis.

### `notebooks`

Contains Jupyter notebooks used for data cleaning, exploratory data analysis, statistical testing, and visualization.

### `slides`

Contains the final project presentation.

### `sql_scripts`

Contains SQL scripts used for database creation and analysis.

### `src`

Contains reusable Python functions for data cleaning and visualization.

# Installation

## Clone the Repository

```bash
git clone https://github.com/jannoelvero/first_project.git
cd first_project
```

## Install UV

For macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Create and Synchronize the Environment

```bash
uv sync
```

## Activate the Environment

For macOS and Linux:

```bash
source .venv/bin/activate
```

For Windows:

```powershell
.venv\Scripts\activate
```

# Conclusion

The analysis shows that Airbnb guest ratings are associated with multiple listing and market characteristics rather than a single factor.

A large majority of listings are highly rated, while poorly rated listings represent only a small proportion of the dataset. Highly rated listings are significantly more expensive than poorly rated listings, and location is significantly associated with both price and guest rating.

Amenities and review volume show statistically significant but weak relationships with ratings. This indicates that simply adding more amenities is unlikely to substantially improve guest satisfaction.

The strongest practical message from the project is that hosts should focus on the overall guest experience. Cleanliness, property condition, accurate listing information, realistic guest expectations, appropriate local pricing, useful amenities, and responsiveness to feedback are more actionable priorities for improving underperforming listings.

The project demonstrates an integrated Python and SQL analytics workflow, moving from raw data preparation through database analysis, statistical testing, visualization, interpretation, and business recommendations.
