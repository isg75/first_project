# Faith, Conflict, and Development: A Global Analysis of Religiosity Across Regions

## Project overview

Religion has undoubtedly played a crucial role in societies and their development, but in recent years, with regional conflicts rising and economic insecurity looming the role and importance of religion is changing. Research has shown that direct exposure to armed conflict can increase individual religiosity in some groups, serving as a coping mechanism (Shai, 2022, J. Econ. Behav. & Org). However, it can have the opposite effect as well; conflict can also lead to religious rejection or disaffiliation, especially when religious institutions are perceived as ineffective. 

Conflict, however, is not the only factor that could influence religious affiliation. Religiosity and Wealth (GDP per capita) can be interconnected; in stable, economically developed countries, religiosity often declines, especially in those marked by scientific rationalisation and a liberal economy (Weber, 1905; Inglehart & Norris (2004; Barro & McCleary (2003)). Similarly to Conflict, wealth can also have the opposite effect. Modernity and the division of labour can foster social isolation and disenchantment, prompting individuals to turn to religion for meaning, support and cohesion (Durkheim,1912; Tocqueville, 1835). 

Moreover, High HDI, urbanisation, and greater access to education are associated with a decline in religiosity (Norris & Inglehart, 2011; Barro & McCleary, 2003

Thus, we want to analyse how conflict, wealth and societal factors (HDI) affect religious affiliation between countries and regions. Understanding the factors associated with these differences can provide insights into broader social and economic patterns.

*Research Question*: How do economic development, conflict, and societal factors influence levels of religious affiliation across regions overtime?

- *Hypothesis 1*: Countries with higher GDP per capita tend to have lower levels of religious affiliation.

- *Hypothesis 2*: Regions experiencing higher levels of conflict tend to show stronger religious affiliation.

- *Hypothesis 3*: There is a negative correlation between HDI and religiosity (high HDI lower religiosity/low HDI high religiosity)


To address this question and test our hypothesis, multiple global datasets were combined and analysed, including data on religious populations, economic indicators, human development, and the socio-economic impacts of war.

The project integrates data from several sources:

1. Religious Populations Worldwide dataset, which provides information on the distribution of major religious groups by country.

2. World Bank GDP dataset, which includes economic indicators such as GDP per capita.

3. Human Development Index (HDI) data from the United Nations Development Programme, capturing broader measures of societal development including education and life expectancy.

4. War Economic & Livelihood Impact dataset, which captures the economic and social effects of major conflicts, including GDP changes and food insecurity rates.

5. World Bank Total Country Population dataset which includes total population per country from 1960 to 2024


## Business Opportunity

This project is developed from the perspective of a political think tank focused on global stability, development policy, and geopolitical risk analysis. Governments, international organisations, and NGOs increasingly rely on data-driven insights to understand the social conditions that may contribute to conflict or instability. Much research has focused on the impact religion and religious affiliation have in shaping political environments; less research has focused on how social, political and economic conditions have shaped religion over the years. 

By analysing how conflict, GDP per capita, and human development indicators relate to religious affiliation across countries and regions, this project aims to provide insights that could support policy research, conflict prevention strategies, and international development planning. Understanding how religiosity changes in response to conflict or economic development can help policymakers anticipate social tensions, migration pressures, and shifts in societal cohesion.

We hope to provide practical applications in areas such as early warning systems for instability, regional risk assessment, and policy recommendations for international development organisations. 

## Variables 

**Categorical**: 

1. **Country**: The name of the country for which the data is recorded. Each observation corresponds to a specific country.
   
2. **Religions** (christianity, judaism, islam, buddhism, hindu, shinto, confus_tao): These variables represent the population counts of the seven largest global religions within each country for a given year. They indicate how many people in a country identify with each religion at that time.

3. **UN Region**: The regional classification of countries according to the United Nations geographic grouping system. Examples include Africa, Asia, Europe, Latin America and the Caribbean, Northern America, and Oceania.

4. **Conflict Present**: A binary variable indicating whether a country is involved in an armed conflict in a given year. A conflict is defined as a situation where a specified number of people have died due to organized violence, and it includes the country where the conflict is occurring.


**Numerical**: 

1. **Year**: The year in which the data was recorded. The dataset includes observations for the years 1990, 1995, 2000, 2005, and 2010, allowing analysis of trends over time.

2. **GDP**: Gross Domestic Product per capita for each country and year. This measures the average economic output per person, providing an indicator of a country's level of economic development.

3. **HDI** (Human Development Index): A composite index measuring a country’s level of human development based on life expectancy, education, and income. It provides a broader indicator of societal development beyond economic measures alone.

4. **Population**: The total population of a country in a given year. This variable represents the total number of people living in the country and is used to contextualize the size of religious populations and calculate religious share.


## Data Cleaning, Transformation, Integration

1. Data Cleaning

- Each dataset was cleaned individually before integration. The main cleaning steps included:

- Standardizing column names to ensure consistency across datasets (all common column titles were the same, all in lowercase, spaces replaced with underscores)

- Checking and converting variables to appropriate data types (e.g., numeric, categorical).

- Removing duplicate records where necessary.

- Handling missing values in key variables.

- Standardizing country names to ensure compatibility across datasets by using the same country/region classification template from the UN

- Filtering datasets to include relevant observations filtering by overlapping years so they all shared a common time frame (1990-2010)

- The cleaned datasets were saved in the data/clean directory.



2. Data Transformation

Additional transformations were performed to prepare the datasets for merging:

- Conflict data was structured to align with country-based analysis.

- Relevant variables were selected from each dataset to reduce unnecessary complexity.

- Inconsistent formats (e.g., percentages, numeric values) were standardized.

- Used UN's region/country classification to ensure all countries and their respective regions followed the same format


3. Data Integration

The cleaned datasets were merged into a unified dataset using common identifiers:

- Country
- Year

The merging process followed a stepwise approach:

The religious population dataset was used as the base dataset.

GDP data was merged using country and year as keys.

HDI data was added to incorporate societal development indicators.

Conflict data was merged to include information on war-related economic impacts

Left joins were used during the merging process to ensure that all observations from the base dataset were preserved while incorporating additional variables where available.

A new column ("conflict_present") was created to present conflict as a binary variable (1 = conflict present, 0 = no conflict)

## Main dataset issues and solutions

Dataset Challenges and Solutions

**Challenge 1**: Limited time coverage in the religious population dataset
The religious population dataset only contained observed data up to 2010, while the project analyzes relationships between religion, economic development, and societal factors in more recent years.

**Solution 1**: Additional datasets were explored to identify sources that contained non-projected religious population data for years beyond 2010. Preference was given to datasets with observed values rather than projections, as projected values could introduce additional uncertainty into the analysis. Ultimately, we decided using a time coverage that overlapped between all datasets (1990-2010)



**Challenge 2**: Mismatched time ranges between datasets. The Human Development Index (HDI) dataset only contains data up to 2022, while the conflict dataset includes conflicts extending to 2025. Ideally, all datasets would cover the same time range for direct comparison.

**Solution 2**: Instead of restricting all datasets to the same time range, the full conflict dataset was preserved in order to retain broader regional and country coverage. Limiting the conflict dataset to 2022 would have removed several conflicts affecting multiple countries and regions, which would significantly reduce the dataset’s analytical value.



**Challenge 3**: Since we used UN's region/country classification and code as a guide to ensure all country names in our datasets were the same to make merging easier, some countries were not included in our study as they were not recognised or included in the UN's country list.  

**Solution 3**:  Countries that were not recognized or included in the UN classification were excluded from the analysis to maintain a consistent and comparable set of country identifiers across all datasets.



**Challenge 4**: Differences in dataset structure and variable naming
The datasets originated from different sources and used different column names, formats, and country naming conventions, which can create issues during merging.

**Solution 4**: Data cleaning and preprocessing steps were performed to standardize column names, harmonize country identifiers, and ensure consistent formatting across all datasets before merging.


**Challenge 5**: Challenge 5: Differences in conflict definitions and dataset coverage. The conflict dataset uses a specific definition of conflict, recording an event only when it results in at least 25 battle-related deaths, which may exclude smaller-scale conflicts captured in other datasets. Additionally, conflicts are attributed only to the country where the fighting occurs, rather than to all countries involved in the conflict. For example, although the United States participated in the Gulf War, it does not appear as a conflict country in years such as 1990 or 1995, since the fighting took place outside its territory. 

**Solution 5**: To address these limitations, we standardized the temporal scope of the analysis to five-year intervals between 1990 and 2010 to ensure consistency across all datasets. While this approach may not capture every conflict event, it allows for a comparable dataset structure across sources. These limitations were acknowledged when interpreting the results, recognising that the dataset may underrepresent certain conflicts or countries indirectly involved in conflicts.



**Challenge 6**: Furthermore, due to limitations in data availability across datasets, the analysis focuses on five-year intervals between 1990 and 2010. As a result, some conflicts that started or ended between these observation years may not appear in the dataset, which may affect the representation of conflicts in certain regions, such as the Balkans in the early 1990s.

**Challenge 7**: When analysing the descriptive statistics for religious_share the maximum value was 340%, which is not possible. What we discovered was how for some countries, the religious population (sum of all religion groups) exceeded the countries total population giving a religious share greater than 100% which is not possible.

**Solution 7**: We capped religious share to ensure religious population could not exceed country population 

## Exploratory Data Analysis

After the datasets were merged, exploratory analysis was conducted to identify patterns and relationships between variables. These patterns and relationships were then visualised using Python data visualisation 



1. Comparing religious affiliation across regions and countries:

The shares of the seven major religions included in the dataset were aggregated by year to observe how global religious composition evolved between 1990 and 2010. This helped identify general trends and assess whether notable shifts occurred during periods associated with conflict.

2. Analyzing the relationship between GDP per capita and religious composition by:

Analysing GDP trends by dominant religion over time: Plotted average GDP for countries grouped by their dominant religion between 1990 and 2010.
Compared GDP development in conflict vs. non-conflict countries to show how GDP evolved over time for different religious-majority countries, separating those with conflict from those without conflict.

Examined religious composition around conflict periods: Compared religious shares before, during, and after conflicts, as well as in countries that did not experience conflict.

Compared economic performance around conflict phases: Average GDP was also visualized across pre-war, during-war, and post-war periods for different dominant religions to observe how conflict might relate to economic changes.

3. Exploring the impact of conflict-related variables on societal conditions:

Compared religious population trends in conflict vs. non-conflict countries: Show how the total religious population and religious share evolved over time (1990–2010) depending on whether countries experienced conflict.

Analyzed regional patterns: Separate plots were produced for Africa, Asia, Europe, Latin America and the Caribbean, Northern America, and Oceania to examine how religious population levels differed between conflict and non-conflict countries across regions.

Examined changes in religious share by region: Additional charts compared the proportion of religious populations (religious share) over time for conflict and non-conflict countries within each region.

- We needed a measure that removed population size effects, as if we were to look at the number of religious populations, larger countries would automatically appear as more religious due to their population size. Thus, we first had to calculate the religious share (proportion of religious populations)

Identified regional differences in conflict dynamics: The visualisations highlight how the relationship between religion and conflict varies across regions, with some regions showing larger differences between conflict and non-conflict countries than others.

4. Statistical testing: The visualisations helped us understand the patterns between religion, HDI, GDP and conflict; nonetheless, it is important to understand that the correlations our graphics showed do not indicate causation. Thus, in an attempt to fully understand the relationships between our variables, we carried out statistical testing.

- For religion (religious share) and conflict (conflict present), we carried out a logistic regression as it was the most suitable test for the data types of each variable (continuous and binary, respectively). The regression results indicated a positive and statistically significant relationship between conflict and the share of religious affiliation.

## Visualisations




## Results

**Hypothesis 1: Countries with higher GDP per capita tend to have lower levels of religious affiliation.**

The results only partially support the hypothesis that higher GDP per capita is associated with lower religiosity. While some patterns suggest that regions with lower GDP tend to have higher religious affiliation, the analysis indicates that conflict exposure is a stronger determinant of economic performance than religion itself. Countries experiencing conflict generally show lower and more volatile GDP growth, due to factors such as infrastructure destruction, reduced investment, and declining labour productivity. In contrast, countries without conflict display more stable and consistent economic growth across all religious groups.

At the same time, conflict appears to influence religious composition indirectly through demographic shocks, including migration, displacement, and population loss. These processes can alter the relative share of religious groups across regions, particularly in areas where conflicts are geographically concentrated. Overall, the findings suggest that the apparent relationship between religion and GDP largely reflects geographic clustering and conflict dynamics, rather than religion directly shaping economic development.

**Hypothesis 2: Exposure to conflict raises religiosity, becoming a coping mechanism:** 

At the global level, the number of religious people remains relatively stable across most regions, with Africa showing a slight increase and Asia consistently representing the largest religious population (Figure 1A). Regional compositions differ: Europe and Northern America are largely Christian, Asia is more religiously diverse, and Africa is split mainly between Christianity and Islam (Figure 1B). However, when analysing religious share (percentage of the population) rather than absolute numbers, clearer trends emerge. Religious affiliation declines in Europe and Northern America, while it remains high and stable in Latin America, Oceania, and Asia. Africa shows a gradual increase, which may partly reflect dataset limitations regarding smaller religions (Figure 1C).

Comparing countries with and without conflict reveals that countries experiencing conflict tend to show slightly higher religious affiliation over time. In most cases, however, changes remain relatively limited, generally within ±10% even in countries with several years of conflict. Some outliers exist, such as Russia, which experienced large fluctuations during the post-Soviet transition, and Liberia, where religious affiliation rose sharply during periods of civil war (Figure 2A). These patterns should be interpreted cautiously given the dataset’s conflict definition and methodological limitations.

Overall, religious structures remain relatively stable across countries, typically dominated by one or two major religions. Christianity and Islam remain the most widespread globally, while parts of Asia are dominated by Hinduism, Buddhism, or Confucian traditions. Countries without conflict generally maintain stable religious proportions, although some countries show larger fluctuations that warrant deeper country-level analysis (Figure 2B).

Statistical testing supports the patterns observed in the visualisations. The regression results indicate a positive but modest relationship between conflict and religious affiliation, with conflict countries showing on average about 4.3 percentage points higher religious share (β = 0.0433, p = 0.004). However, the relatively small effect size suggests that conflict alone cannot explain differences in religiosity, and that other factors such as economic development, demographic change, and migration likely also shape these patterns.


Moreover, the analysis suggests that conflict influences religious composition indirectly through demographic shocks such as migration and population displacement. Countries experiencing conflict show greater fluctuations in religious distribution compared to peaceful regions. However, GDP growth patterns appear more strongly associated with conflict exposure than with dominant religion. While religion correlates with economic development due to geographic clustering, conflict intensity is the primary factor explaining variations in GDP growth.


**Hypothesis 3**: There is a negative correlation between HDI and religiosity (high HDI lower religiosity/low HDI high religiosity)


The analysis of the relationship between the Human Development Index (HDI) and dominant religion share reveals a statistically significant but very weak positive relationship. Both the Spearman correlation (ρ ≈ 0.10) and the OLS regression results indicate that countries with higher levels of human development tend to have slightly higher shares of a dominant religion. However, the explanatory power of the model is extremely low (R² ≈ 0.025), meaning that HDI explains only about 2.5% of the variation in religious dominance across countries. This suggests that economic and human development alone do not meaningfully determine the concentration of religious affiliation in a country. Instead, religious dominance is likely shaped primarily by historical, cultural, and demographic factors, such as colonial history, migration patterns, and long-standing religious traditions. Therefore, while the relationship exists statistically, it is not substantively strong enough to suggest that development significantly drives religious concentration.


In contrast, the relationship between HDI and the presence of conflict shows a stronger and more meaningful pattern. The logistic regression results indicate that HDI is a highly significant predictor of conflict probability, with a large negative coefficient.
This means that higher levels of human development are associated with a substantially lower probability of conflict. The model’s pseudo R² of approximately 0.125 suggests that HDI alone explains about 12.5% of the variation in conflict occurrence, which is relatively meaningful given the complexity of factors that influence conflict. The results therefore support a widely documented pattern in political economy and development research: countries with higher levels of development tend to experience fewer conflicts. Higher HDI is typically associated with stronger institutions, better education, improved economic opportunities, and greater political stability, all of which reduce the likelihood of violent conflict.

Taken together, the results highlight that human development plays very different roles depending on the societal outcome being examined.
In the case of religious dominance, development has little explanatory power, suggesting that religion is primarily shaped by long-term cultural and historical processes. In the case of conflict, development shows a clear and meaningful association, with higher HDI strongly linked to a lower probability of conflict. Overall, these findings suggest that while development alone does not reshape cultural structures such as religion, it appears to significantly contribute to social stability and the reduction of conflict risk.

## Conclusions: 

This study examined how economic development and conflict influence levels of religious affiliation across regions over time. The results provide partial support for both hypotheses. Wealthier regions, particularly Europe and Northern America, tend to show declining religious affiliation over time, suggesting that higher levels of economic development are associated with lower religiosity. However, this relationship is not uniform across all regions, indicating that economic development alone does not fully explain variations in religiosity.

The analysis also finds moderate evidence that conflict is associated with slightly higher levels of religious affiliation. Countries experiencing conflict show, on average, about 4.3 percentage points higher religious share, although the effect is relatively small and religious structures remain largely stable in most countries. Overall, the findings suggest that religiosity is influenced by both economic conditions and conflict exposure, often indirectly through factors such as migration, displacement, and broader regional dynamics.

Taken together, the results highlight that human development plays very different roles depending on the societal outcome being examined.
In the case of religious dominance, development has little explanatory power, suggesting that religion is primarily shaped by long-term cultural and historical processes. In the case of conflict, development shows a clear and meaningful association, with higher HDI strongly linked to a lower probability of conflict. Overall, these findings suggest that while development alone does not reshape cultural structures such as religion, it appears to significantly contribute to social stability and the reduction of conflict risk.

## Next steps and practical recommendations 


1. Prioritise conflict prevention and stabilisation policies: Since the analysis shows that conflict has a stronger impact on economic performance than religion, governments and international organisations should prioritise conflict prevention, mediation, and post-conflict reconstruction. Reducing conflict intensity can help protect infrastructure, maintain investment, and support long-term economic stability.

2. Integrate demographic and migration dynamics into policy planning: Conflict often affects religious composition indirectly through migration, displacement, and population loss. Policymakers should incorporate demographic data and refugee movements into development and social planning to better anticipate changes in population structure and social cohesion.

3. Address structural drivers of instability rather than focusing on religion alone: The findings suggest that religion itself is not the primary driver of economic development or conflict. Instead, policies should focus on structural factors such as economic inequality, governance quality, and regional instability, which are more likely to influence both conflict risk and long-term development outcomes.


## Datasets 

Final dataset: http://localhost:8890/lab/tree/Desktop/Week4/first_project/data/clean/final_dataset.csv


Final dataset including religious population and religious share: http://localhost:8890/lab/tree/Desktop/Week4/first_project/data/clean/final_dataset_religious_share.csv


## Resources 

https://www.kaggle.com/datasets/thedevastator/religious-populations-worldwide?select=ThrowbackDataThursday+201912+-+Religion.csv
https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?end=2024&start=2024&view=map&year=2024
https://github.com/openwashdata/worldhdi
https://www.kaggle.com/code/lalit7881/war-economic-livelihood-impact-dataset#Import-dataset
https://www.prio.org/data/5?utm
https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv

https://trello.com/c/kqFlipwv/17-day-1-get-the-data

## Presentation link
https://docs.google.com/presentation/d/1TuB6IdBKZEBOSkqFy5jF60my7jVQU6la2mYfpI4NCdI/edit?usp=sharing


