# Project overview
Objective:
Turning a “blind” travel business policy into a data-driven one.

Our problem statement (draft - subject to change):
Many travel agencies / tourism service providers struggle to use their historical booking/trip data effectively. Without structured insight into when, where, and for how long travelers go, companies lack evidence to:
optimize marketing and promotions by season / region,
forecast demand to negotiate with accommodation or transport providers,
tailor travel packages to traveler behavior (e.g. trip duration, popular destinations), or
detect under-served / emerging travel destinations that might deserve new offerings.

Business Use-Cases:
Demand forecasting & capacity planning: by anticipating high-season destinations and months.
Marketing & promotions optimization: align campaigns with seasons, demographics, destinations.
New product/offer development: design destination-specific travel packages (city-break, long trip, destination-bundle) based on observed traveler behavior.
Cost & supplier negotiation leverage: if you know high-traffic destinations ahead of time, you can negotiate better deals with hotels, transport providers, or local vendors. This is similar to what firms in “business travel analytics” aim for.

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

# Hypothesis 
1. Seasonality patterns vary between continents Europe and Asia
2. Different traveler demographics (age, nationality) show different destination and trip duration preferences.
3. Travelers choose different accommodation types for different trip durations, or based on their age.
4. Transportation type preferences differ per travelers’ age
5. Accommodation and transportation prices in high demand continents follow seasonality patterns.

# Dataset 
https://www.kaggle.com/datasets/rkiattisak/traveler-trip-data

## Main dataset issues & Solutions provided
- Dataset had no major issues
- Needed some basic cleaning across some columns, especially the numerical ones, where we could find currency symbols, text, and commas.
- We needed to prepare and format the date columns in a ways that we can extrapolate new columns specifying the month, so that we can use it in seasonality research.
- The column "destination" was appending city and country together, we actually decided to split that into two new columns with separate information for each. However, many country information was missing (almost the half), therefore we needed to import a library that gets those values. Before that, we needed to format and replace a lot of the cities values in a way that they could be understood by the library in order for it to work.
- We also created a "Boolean" type column called "is_intercontinental_trip", essentially assessing whether the nationality of the traveler and their destination were within the same continent.
- The data set is not big enouhg to be able to draw confident conclusions about different cities, countries, or nationalities of travelers. Therefore, for each of these three columns we created a new column that clustered them into continents.

# Conclussions
- The dataset is limited, therefore, we need to be careful with the conclusions we make.
- Businesses in Europe and need to adjust their pricing for the month of May till September, in order to enjoy a more balanced demand. For Asian businesses, those month would be March, April, and September.
- For months of low demand, do marketing campaigns and promotions, highlighting the low prices that a traveler could benefits for. This way, businesses can create demand and revenue, even in months with historically low demand.
- To better address the needs of Student-Early Professionals, create discount packages for short term trips in Asia, using Hostels as a primary accommodation. For the Young Professionals, create long trip offerings focusing on Asia and Oceania. For Young Parents, focus on weekend getaways in Europe using the train.
- Follow the demand curves, and make sure to buy less of equipment needed during low demand periods, and buy, early in advance, using economies of scale discounts when you expect a high demand.

# Next steps
- We would like to find more observations on trvel trip data, especially for older generations, in order to be able to have a more statistically signigicant reserarch outcome, while further curating new products for a larger subset of traveler demographics.
