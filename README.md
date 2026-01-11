# Project overview

**Airline Passenger Satisfaction**

1. Problem Statement:
   
The core problem this project addresses is: Identifying the key drivers of passenger satisfaction and dissatisfaction within an airline's service ecosystem.

Airlines need to understand which operational, service, and demographic factors most significantly influence a passenger's overall rating of their experience (Satisfied vs. Neutral or dissatisfied). 
This understanding is crucial for strategic resource allocation, service improvement, and customer retention.

2. Dataset Source and Content

Feature:                 	      Description
Source:       	                  Typically sourced from passenger surveys collected post-flight. (The uploaded file references a Kaggle dataset).
Unit of Analysis:	              An individual flight or passenger survey response.
Data Types	Categorization:       Gender, Customer Type, Type of Travel, Class.
Ordinal:                          Over 10-15 ratings (e.g., In-flight Wi-Fi, Seat comfort, Food and drink) on a 1-5 scale.
Numerical:                        Age, Flight Distance, Departure/Arrival Delay in Minutes.
Target Variable:	              Satisfaction (Categorical: Satisfied / Neutral or dissatisfied).


3. Project Goals (Analytical Objectives)
The project aims to achieve the following:

Prediction:                       Build a classification model (e.g., Logistic Regression, Decision Tree, etc.) capable of accurately predicting whether a new passenger will be "Satisfied" or "Neutral/Dissatisfied" based on their flight      
                                  characteristics and service ratings.

Feature Importance:               Determine the top features (e.g., Wi-Fi quality, Cleanliness, Delay duration) that have the strongest correlation and predictive power for overall satisfaction.

Segmentation:                     Analyze satisfaction patterns across key customer segments, particularly: Loyalty (Loyal Customer vs. disloyal Customer), Travel Purpose (Business travel vs. Personal travel), Travel Class (Business vs. Eco)


4. Methodology and Techniques Used
The analysis followed a standard data science pipeline:

Data Preprocessing:                     Handled missing values (imputation), cleaned inconsistent data types, and scaled numerical features using MinMaxScaler.

Exploratory Data Analysis (EDA):        Used value_counts() and groupby() to understand data distributions and initial segment satisfaction rates.

Statistical Analysis:                   Employed Correlation Analysis to measure linear relationships and a T-test to statistically validate the impact of key factors (like delays) on satisfaction.

Visualization:                          Utilized Seaborn and Matplotlib to create clear visualizations (Bar Plots, Heatmaps, KDE Plots) to communicate segment differences and feature relationships.


5. Expected Business Impact
   
The results of this analysis provide the airline with actionable intelligence to drive business decisions:

Prioritization:           Allocate investment to service factors with the highest positive correlation to satisfaction (e.g., upgrading in-flight entertainment or Wi-Fi infrastructure).

Operational Focus:        Target areas where dissatisfaction is highest (e.g., mitigating minor departure delays) to maximize customer experience per dollar spent.

Marketing & Strategy:     Customize service offerings and marketing campaigns based on loyalty and travel purpose (e.g., developing specific retention strategies for disloyal passengers).


# Questions 
This dataset is rich with possibilities because it contains both operational factors (delays, distance) and subjective service ratings. The questions were grouped into four main analytical categories: Predictive Modeling, Segmentation, Operational Insight, and Service Quality.

I. Predictive Modeling:            Which specific service rating (e.g., In-flight Wi-Fi, Cleanliness) is the single strongest predictor of overall satisfaction?

II. Segmentation:                  What is the percentage difference in satisfaction between Loyal Customers and disloyal Customers, and do these two groups cite different reasons for their satisfaction/dissatisfaction?

III. Operational Insight:          What is the precise number of minutes of delay after which the probability of a passenger being "Neutral or dissatisfied" increases most sharply?

IV. Service Quality:               If the airline were to improve one service rating by one point (e.g., from 3 to 4), which service provides the greatest return on investment in terms of increased satisfaction?

# Dataset
Airline Passenger Satisfaction Survey, Kaggle.com train_csv

## Main dataset issues
The Dataset was largely cleaned which made the analysis easier and straightforward. This notwithstanding, there were some Dataset issues that we had to deal with. These dataset issues included the following:

1. The Satisfaction column contained only strings
2. The Age column had too many information
3. The column named Flight Distance also had too many information
4. Lastly the first dataset selected on day 1 was not reliable and full of synthetic errors 


## Solutions for the dataset issues
Having encountered the above dataset issues a number of solutions were employed to address the challenges. Some of the solutions included the following:

1. We created a binary column based on the existent Satisfaction column, which was string.

2. Aggregation and groupings were employed in relation to the Age and Flight Distance columns

3. One working day was missed, because of unrealiable dataset. It was a synthetic dataset, therefore it was unrealistic.

# Conclussions

The overall conclusion is that Customer Loyalty and Quality In-Flight Service  are the primary drivers of satisfaction, while operational failures (specifically delays) are the primary drivers of dissatisfaction.

# Next steps

To maximize overall passenger satisfaction, it was recommended that the airline should adopt a dual strategy:

Service Excellence: Continuously improve and invest in in-flight amenities (Wi-Fi and entertainment) as these yield the highest returns on positive sentiment.

Operational Reliability: Treat on-time performance as a non-negotiable factor. Focus resources on minimizing all delays, as even small disruptions create a disproportionately large increase in dissatisfaction, especially among customers who are not already loyal.
