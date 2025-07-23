Project Title:  BARCELONA RESTAURANT OPPORTUNITY

# Project overview
Barcelona is known for its dynamic culinary scene and diverse neighborhoods, each with distinct characteristics. However, launching a restaurant in this competitive environment requires more than intuition demands a clear understanding of local income, tourist activity, and potential saturation.
This project aims to identify the most strategic district in Barcelona to open a new restaurant, using a data driven approach that balances economic indicators and tourism potential.  Choosing the right district can provide the perfect mix of foot traffic, affluent residents, and manageable competition.

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
# Dataset 
We Downloaded:
1) “Hotels in the city of Barcelona” 2020
https://opendata-ajuntament.barcelona.cat/data/en/dataset/allotjaments-hotels
2) “Demographic indicators. Population density (inhabitants / ha) of the city of Barcelona” 2022
https://opendata-ajuntament.barcelona.cat/data/en/dataset/est-densitat
3) “Disposable income of households per capita(€) in the city of Barcelona” 2021
https://opendata-ajuntament.barcelona.cat/data/en/dataset/renda-disponible-llars-bcn
We used APIs for:
Reddit mentions for different food types in r/Food (steak, pizza, burger, pasta, ramen, sushi, paella, Korean bbq, tapas)
Google Reviews of top 55 restaurants in Barcelona (name, rating, address, longitude, latitude, type)

## Main dataset issues
- Paywall for APIs. We consistently ran into APIs that were only accessible with significant payments.
- API restrictions. We had to accept only loading 55 restaurants as the API was restricted.
- The districts were in the address column in the google reviews data frame to merge them with the others. The district names also had slightly different wording that had to be adapted manually.

## Solutions for the dataset issue-To merge the data frames, the district name had to be extracted from the adress column in the google review data frame. The district names also had slightly different wording that had to be adapted manually.-
For the APIs we decided to also extract information from reddit to gain more variety in data

## Strenghts and Weaknesses
Strengths:
The dataset is well-structured and tabular, making it easy to load and manipulate.
It contains several numeric columns like rating, reviews, income, and density, which support statistical analysis.
Latitude and longitude enable spatial techniques such as clustering or heatmap creation.
It includes categorical and textual data such as district, neighbourhood, and types, allowing for grouping and classification.
Weaknesses:
The sample size is small, which limits the reliability of any statistical conclusions.
The variable rating is subjective, and may not fully capture business performance.
The column types is unstructured, with mixed labels and formatting, requiring significant cleaning.
The dataset lacks a time dimension, preventing any time series or trend analysis.

# Question
¿What are the ideal locations and most suitable food type for opening a premium restaurant in Barcelona?

# Methodology
1) Loading data: API and dowloading datasets
2) Cleaning data, merged dataframes, delt null and duplicates: numpy and pandas
3) Charts, plots, correlation table: matplotlib, seaborn
4) Heatmap: folium ...

# Conclussions
Our analysis identified three standout districts: Eixample, Sarrià-Sant Gervasi, and Les Corts—each with strategic potential depending on the target market.
Ultimately, Eixample emerged as the ideal location, it offers the best balance of year-round demand, high tourist flow with the highest hotel concentration, and strong rating potential, while Les Corts and Sarrià-Sant Gervasi share similar income levels and quality indicators, their lower population density suggests reduced foot traffic—making Eixample the most compelling choice for visibility, volume, and long-term success.
Further questions
What pricing strategy fits the income level and tourist profile of the area?
When is demand highest in this area?


Presentation: https://docs.google.com/presentation/d/1Ny8zftGfeMyTNozQgHw9vF9VJ0c4j-FLqNYIiMX6Q2w/edit?slide=id.g36e2651165f_2_245#slide=id.g36e2651165f_2_245
Extra sources:  https://trello.com/b/h3utlBtt/firstproject
