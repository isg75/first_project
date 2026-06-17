# Project name: Amazon Marketplace Decoding

# Project Overview
This project analyzes an Amazon product dataset (source: Kaggle) to understand how pricing, discounting, and market saturation influence customer satisfaction.
The goal is to validate or refute three business‑driven hypotheses using exploratory data analysis, visualization, and statistical reasoning.

# Business Hypotheses
Hypothesis 1 — Premium Pricing Signals Premium Quality
Higher product prices naturally signal higher quality, leading to better user sentiment.

## This analysis explores:

### Hypothesis 1 — 
- How reviewer sentiment varies across price segments

- Whether premium products consistently receive higher rating

- How price influences perceived value and user experience?

### Hypothesis 2 — 
- Discounts Act as Emotional Anchors
Large discounts create a psychological “deal effect,” increasing customer satisfaction and ratings.

This analysis investigates:

- Whether higher discount percentages correlate with higher ratings

- Whether discount‑driven purchases show inflated sentiment

- How discount depth affects rating distribution

### Hypothesis 3 —
- Underserved Niches Show High Review Volume but Low Satisfaction
- Categories with few products but many reviews and low ratings indicate unmet customer needs.

## This analysis identifies:

Categories with low product availability but high engagement

Segments where customers express dissatisfaction despite high demand

Potential opportunities for new product development

# Repository Structure
├── README.md                                   <- Project overview and business roadmap
├── data/
│   └── amazon.csv                              <- Raw source dataset from Kaggle
├── notebooks/
   └── eda_claire.ipynb                         <- Exploratory data analysis & custom plotting pipeline
   └── explore_clean_data_zidene.ipynb          <- Exploratory data analysis & custom plotting pipeline
   └── functions.py                             <- all functions used in the project
├── slides/
   └── project_slides url                       <- Project presentation slides 

└── figures/
    ├── fig1_price_vs_rating.png                <- Price segmentation bar charts
    ├── fig2_discount_trap.png                  <- Dual-axis discount volume/sentiment cliff
    └── fig3_niche_quality_price.png            <- Opportunity scoring & niche candidate analysis
    ├── fig4_categories_rating                  <- User ratings by prodcut category
    └── fig5_rating_distribution_by_price.png   <- Evaluating rating with regards to product pricing

project_slides url: https://docs.google.com/presentation/d/1or2I0dxIeo96H9ww6bakcm8ZBFywKj_Gzh_ZptvTnnY/edit?slide=id.g3e4aa31e4e8_0_1#slide=id.g3e4aa31e4e8_0_1
# Tools & Libraries
pandas,matplotlib.pyplot, seaborn, numpy

Jupyter Notebook

Kaggle dataset (Amazon product metadata + ratings)

Git for version control

# Methodology
- Data ingestion from Kaggle

- Cleaning & preprocessing

- Handling missing values

- Creating price and rating segments

- Normalizing discount rates

- Exploratory Data Analysis

- Sentiment distribution

- Price vs rating relationships

- Discount vs rating correlations

- Hypothesis testing

- Visual evidence

- Statistical indicators

# Insights & recommendations

## Key Findings (Summary)
### Hypothesis 1 — 
Premium products show higher proportions of excellent ratings and fewer poor reviews, indicating that price positively influences perceived quality.

### Hypothesis 2 — 
Large discounts correlate with slightly higher ratings, but the effect is not uniform across categories. Emotional anchoring exists but is not the dominant driver.

### Hypothesis 3 —
Several categories show low product counts, high review volume, and low satisfaction, signaling underserved niches with strong market potential.

# How to Run the Project
Place raw data in data/raw/

Run cleaning scripts or notebooks to generate data/cleaned/

Open notebooks in /notebooks to reproduce analysis

Import helper functions from src/functions.py

Example:

python
from src.functions import segment_price, plot_rating_distribution

# Data Source
Dataset obtained from Kaggle.com  
(Include link if allowed by Kaggle license)