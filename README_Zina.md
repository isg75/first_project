# Project overview
This project analyzes **global Michelin-starred restaurants** (1, 2, and 3 stars) to understand patterns in:
- Cuisine type vs Michelin star level
- Geographic distribution across regions and major cities
- Price trends by star rating
- Public reviews and their alignment with Michelin ratings

The datasets were concatenated, cleaned, and enriched with:
- Average price (`price_mean`)
- Review rating and count metrics

# Installation

1. **Clone the repository**:

```bash
git clone https://github.com/ArrimachNasser/first_project.git

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

# Questions 
1. Do certain cuisines have a higher probability of receiving 3 stars?
2. Which regions host the most starred restaurants?
3. How does the average price vary between 1, 2, and 3 stars?
4. Do public reviews align with Michelin star ratings?

# Dataset 
We used three primary datasets:
- `one-star-michelin-restaurants.csv`
- `two-stars-michelin-restaurants.csv`
- `three-stars-michelin-restaurants.csv`

**Additional sources / enrichment**:
- MICHELIN Guide for The restaurants' price ranges index
- Online Review information using API 

## Main dataset issues
- Missing values in `price` column for some restaurants
- Inconsistent cuisine naming (e.g., "French cuisine" vs "French")
- Some restaurants incorrectly had five dollar symbols ($$$
- Special characters in restaurant names

## Solutions for the dataset issues
- Imputed missing prices with the **median price** per star level
- Normalized cuisine names by lowercase, stripping spaces, and mapping variants to a single category
- Removed duplicates based on `name + city`
- Created a `major_city` flag using top city populations
- Special Characters: Used 'unidecode' to clean restaurant names of accents and special characters
- Inconsistent cuisine naming: Reduced over 100 cuisine types into ~10 coherent groups
- Geographic Organization: Grouped and ordered suburbs by city and region for clarity
- Symbol Inconsistencies: Fixed entries with too many $ symbols, removed extra spaces and hidden characters
- Handeling Missing Prices: Filled missing values using per star category.

# Conclusions
- New York, Hong Kong, and San Francisco are major culinary and cultural hubs that attract Michelin-star.
- New York leads in 1-star and 2-star Michelin restaurants, offering a diverse array of high-quality dining.
- Hong Kong, excels in 3-star Michelin establishments, indicating a focus on elite dining experiences.
- Among 3-star Michelin restaurants, the dominant cuisines are contemporary, French, and Chinese.
- Average price increases with star level, most 3-star restaurants tend to be the most expensive
- Among all cuisines, Austrian cuisine is the most expensive on average.

# Next steps
- Predict Michelin star level using machine learning
- Include chef profiles for deeper insights
- Analyze yearly trends using the `year` column
