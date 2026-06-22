# EncoreWorks: Supporting Longer Careers in Aging Societies

## Executive Summary

This project explores how aging societies can sustain economic productivity by unlocking the potential of workers aged 50+, forming the foundation for EncoreWorks, a data-driven workforce strategy platform.

Using global datasets from the World Bank, including the World Development Indicators and Human Capital Index, the analysis examines how demographic aging, labor force participation, and human capital investment interact across countries. Rather than treating aging as a constraint, the project identifies conditions under which economies successfully maintain productivity despite shrinking working-age populations.

The findings show that productivity outcomes are less dependent on age demographics alone and more strongly linked to investment in skills, education, and workforce inclusion. Countries that actively support lifelong learning and labor participation demonstrate greater economic resilience.

Building on these insights, EncoreWorks is positioned as a scalable solution to help organizations adapt to demographic change. By combining workforce analytics, reskilling pathways, and knowledge transfer tools, the platform enables companies to retain experienced talent, reduce skill gaps, and transform longer careers into a strategic advantage.

## Project Structure

```
first_project/
│
├── data/
│   └── raw/                        # Raw datasets from the World Bank
│       ├── merged.csv
│       ├── WB_HCI.csv
│       ├── WB_HCI_DATADICT.csv
│       ├── WB_HCI_WIDEF.csv
│       ├── WB_HCP_EMP_2WAP_A.csv
│       ├── WB_HCP_EMP_2WAP_A_DATADICT.csv
│       ├── WB_HCP_EMP_2WAP_A_WIDEF.csv
│       ├── WB_WDI.csv
│       ├── WB_WDI_DATADICT.csv
│       └── WB_WDI_WIDEF.csv
│
├── figures/                        # Generated visualizations
│   ├── Age top5_bottom5 graph.png
│   ├── Aging-Level_Aging-Speed.png
│   ├── Fastest-Aging-Societies_2010-2018.png
│   ├── GDP-HCP bottom5 age.png
│   ├── GDP-HCP top5 age.png
│   ├── HCP-HCI-AGE plot graph.png
│   ├── HCP-HCI-Age-GDP Bubble Graph.png
│   └── The World's Demographic Divide_2010-2018.png
│
├── notebooks/
│   ├── data_cleaning_alex.ipynb
│   ├── data_cleaning_beatriz.ipynb
│   ├── data_cleaning_viz_rachel.ipynb
│   └── merged.csv
│
├── slides/
│   ├── EncoreWorks_Prezi.pdf
│   └── EncoreWorks_Prezi.pptx
│
├── src/
│   └── project_template/
│       ├── __init__.py
│       ├── data_prep.py
│       ├── features_beatriz.py
│       ├── features_rachel.py
│       └── plots.py
│
├── config.yaml
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── .python-version
└── uv.lock
```

## Project overview
Many countries are experiencing rapid population aging. As the share of people over 65 increases, the working-age population shrinks, creating pressure on economic productivity, pension systems, and labor markets.

However, some countries manage to maintain productivity despite aging populations. This suggests that the real challenge is not aging itself, but how effectively societies enable people to remain productive throughout longer lives.

This project explores the relationship between aging populations, labor force participation, human capital investment, and productivity in order to identify patterns that help economies sustain growth.

## Business Question 
How can organizations and countries unlock the productive potential of workers aged 50+ in aging societies to sustain economic growth and workforce participation?

## Objectives
The main goals of this project are:

* Analyze the impact of aging populations on workforce participation.

* Explore the relationship between human capital investment and productivity.

* Identify countries that successfully maintain productivity despite demographic aging.

* Extract insights that could help organizations better integrate older workers into the workforce.

## Target Customer
The potential users of the insights generated in this project include:

* Companies facing labor shortages

* HR departments managing workforce planning

* Governments dealing with demographic aging

* Organizations interested in reskilling programs for older workers
* Workers seeking to redefine their professional path later in their careers

## Business Model 

### Product 
A SaaS platform that helps companies manage and extend the careers of employees aged 50+ through workforce analytics, reskilling, and knowledge transfer.

### Key Features
Workforce Analytics Dashboard: analyzes age distribution, predicts retirement risk, and identifies critical skill gaps.

Reskilling Programs: personalized training recommendations to help senior employees transition into new roles.

Knowledge Transfer Tools: mentoring programs and systems to capture and share expertise before retirement.


This platform would help organizations:

* Analyze workforce demographics

* Identify roles suitable for experienced workers

* Recommend reskilling pathways

* Support age-inclusive workforce strategies

* Retain institutional knowledge within companies

Our model is **sector-agnostic**; it’s designed to keep the entire 50+ workforce productive. But what makes it truly powerful is its ability to include **everyone**, including those in physical roles who need a path into more sustainable positions. By looking at the 2010-2018 cycle, we see that this isn't just a social project—it's the **blueprint for economic resilience**.

## Dataset 
World Development Indicators (WDI) 
https://data360.worldbank.org/en/dataset/WB_WDI 
Human Capital Index (HCI)
https://data360.worldbank.org/en/dataset/WB_HCI
Labor Force Participation Rate (%) Indicator
https://data360.worldbank.org/en/indicator/WB_HCP_EMP_2WAP_A

### Data Sources
Our analysis combines two global datasets from the World Bank’s open data platform. These datasets provide standardized indicators across countries, allowing for reliable cross-country comparisons. Our project is doing **cross-country** macro analysis.

The World Development Indicators (WDI) dataset is one of the World Bank’s primary databases for global development statistics. It aggregates internationally comparable data on economic performance, demographics, and labor markets for more than 200 countries. From this dataset, we extracted indicators that measure demographic aging, workforce participation, and economic productivity.

The Human Capital Index (HCI) dataset focuses specifically on the productive potential of a country’s population. It measures how effectively countries develop human capital through education and health outcomes. The dataset includes indicators such as the Human Capital Index score, learning-adjusted years of schooling, and adult survival rates.

The Labor Force Participation Rate indicator is the percentage of the working-age population that is economically active (either employed or actively seeking employment). It is calculated by dividing the labor force (the sum of employed and unemployed persons) by the total working-age population and multiplying the result by 100.
Using both datasets allows us to examine how demographic change, workforce participation, and human capital investment interact across countries.

### Data Analysis Focus
Our analysis investigates the relationship between:

* Aging population (WDI)

* Labor force participation (HCP)

* Human capital investment (HCI)

* Economic productivity (GDP)

By comparing countries, we aim to identify which strategies allow economies to remain productive despite demographic aging.

### Methodology
The project follows these main steps:

1- Data collection

2- Data cleaning and preprocessing

3- Exploratory Data Analysis (EDA)

4- Data visualization

5- Insight generation and interpretation

### Main dataset issues

During the data preparation phase, we encountered several challenges that required cleaning and preprocessing before performing the analysis.


- Inconsistent structures across datasets:
The three datasets used in this project contained different variables, naming conventions, and structures. This made direct merging impossible without prior harmonization.

- Missing values across indicators:
Some indicators were not available for all countries or for all years, which created gaps in the data that had to be addressed before analysis.

### Solutions for the dataset issues
To ensure reliable analysis and comparability across countries, the following steps were taken:

- Data harmonization:

Column names and formats were standardized across datasets to enable successful merging.
The three datasets used in this analysis — the Human Capital Index (HCI), the World Development Indicators (WDI), and the Human Capital per Person (HCP), all sourced from the World Bank — did not share standardized country names, nor did they contain identical country coverage. Country names varied across datasets (for example, differing use of abbreviations, articles, or spellings), and the total number of countries represented differed between them. To address this, country names were standardized across all three datasets, and only countries present in all three were retained for analysis. Countries appearing in one or two datasets but not all three were excluded, ensuring consistency and comparability across the merged dataset.

- Column selection and cleaning:

Only the indicators relevant to the research question were retained, while unnecessary columns were removed to simplify the dataset.

- Handling Missing Values:

For the purpose of our hypothesis testing, we focused our analysis on the top 5 and bottom 5 countries with the highest aging population ratios. 

Although some indicators contained missing values, we decided to keep them as null values because they did not affect the specific variables used in our core analysis. Removing these rows would have unnecessarily reduced the dataset without improving the reliability of our results.

If the missing values had impacted the variables central to our hypothesis, we would have complemented the dataset by sourcing the missing information from external data sources.

***Data Availability Note***

Three countries could not be included in HCI-based calculations due to insufficient official data. Zambia and Monaco were identified in our initial top 5 and bottom 5 age rankings but lacked reliable HCI figures — for Zambia, the earliest available World Bank HCI estimate dates to 2017, and Monaco is absent from the dataset entirely (source: World Bank Human Capital Data Portal). The Central African Republic, brought in as a substitute for Zambia, similarly had no available HCI data in either the World Bank or Penn World Table databases (source: Penn World Table 11.0 via FRED). All three countries were removed from the analysis and not considered further, with the next available ranked country used as a replacement.

***Data Standardization Note***

The three datasets used in this analysis — the Human Capital Index (HCI), the World Development Indicators (WDI), and the Human Capital per Person (HCP), all sourced from the World Bank — did not share standardized country names, nor did they contain identical country coverage. Country names varied across datasets (for example, differing use of abbreviations, articles, or spellings), and the total number of countries represented differed between them. To address this, country names were standardized across all three datasets, and only countries present in all three were retained for analysis. Countries appearing in one or two datasets but not all three were excluded, ensuring consistency and comparability across the merged dataset. All three datasets were sourced from the World Bank Open Data portal.

## Conclusions
Population aging is reshaping labor markets across many economies. Our analysis shows that while some countries already face high shares of older populations, aging alone does not determine economic performance. Instead, the ability of societies to maintain productivity depends largely on how effectively they invest in human capital and support workforce participation throughout longer lives.

By combining demographic data, labor force participation indicators, and the Human Capital Index, we observe that countries with stronger investment in education, skills development, and workforce inclusion are better positioned to sustain economic productivity despite aging populations.

These insights form the foundation of EncoreWorks, a platform designed to help organizations adapt to demographic change. By leveraging workforce analytics, reskilling pathways, and knowledge-transfer tools, EncoreWorks aims to help companies retain experienced workers, extend productive careers, and turn longer life expectancy into an economic advantage rather than a constraint.

## Next steps
Population aging is expected to continue accelerating as healthcare improvements and longer life expectancy extend working-age lifespans across many countries.

Future research could expand this analysis by:

- Including more recent data to capture post-2018 demographic trends

- Exploring sector-level differences in aging workforces

- Investigating policy interventions that successfully extend workforce participation

- Developing predictive models to estimate the economic impact of aging populations

Understanding how societies adapt to demographic aging will be critical for building sustainable labor markets and resilient economies in the coming decades.

## Presentation
https://prezi.com/view/feab0zSP9aHHnHnQMMmw/

## External resources
https://blog.pwc.lu/how-much-can-the-older-workforce-impact-the-oecd-economies/
https://fred.stlouisfed.org/series/HCIYISZMA066NRUG
https://humancapital.worldbank.org/en/home
https://www.ilo.org/publications/employment-trends-youth-middle-east-and-north-africa
https://www.ilo.org/publications/major-publications/global-employment-trends-youth-2024

## Installation requirements for contributors:

1. **Clone the repository**:

```bash
git clone https://github.com/rachelv2/first_project.git
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
