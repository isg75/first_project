## 💤 Sleep Health & Lifestyle Analysis
#### Business Case: Predicting Sleep Disorders


### 📌 Project Overview
This project analyzes a Sleep Health & Lifestyle dataset to identify key factors associated with sleep disorders (Insomnia and Sleep Apnea).
The goal is to understand how lifestyle, physiological metrics, and stress levels contribute to sleep disorder risk and to support early intervention strategies.


### 🎯 Business Problem
Sleep disorders increase medical costs, stress, and reduce quality of life.
Identifying high-risk individuals early enables:
- Preventive healthcare
- Reduced diagnosis costs
- Targeted wellbeing programs


### ❓ Research Questions
- Which lifestyle and physiological factors correlate with sleep disorders?
- Can stress, BMI, activity, and sleep patterns predict disorder presence?
- What differentiates insomnia from sleep apnea?


### 🧪 Hypotheses
#### Primary Hypothesis (H1)
Individuals with high stress, high BMI, low sleep duration, and poor sleep quality are significantly more likely to have a sleep disorder.
**H0:** Sleep disorder presence is independent of these factors.

#### Secondary Hypotheses
- **H1a:** Obesity increases likelihood of sleep apnea. 
- **H1b:** Higher stress correlates with insomnia. 
- **H1c:** Sleeping <6 hours increases disorder risk.
- **H1d:** Low physical activity (<40 min/day) increases disorder prevalence. 
- **H1e:** High heart rate / BP increases apnea risk. 


### 🧹 Data Cleaning Summary
- Checked for missing values, incorrect data types, and duplicates.
- Standardized column names and trimmed string formatting.
- Normalized inconsistent categories (e.g., "Normal" vs "Normal Weight").
- Split Blood Pressure into numeric Systolic and Diastolic columns.
- Converted all relevant columns to numeric types.
- Filled missing Sleep Disorder values with "No Disorder".
- Removed duplicate rows (242 duplicates dropped).

Final result: a clean, consistent dataset ready for analysis.

### 📊 Exploratory Data Analysis (EDA)
Univariate and bivariate analysis was performed to understand data distributions and variable relationships.
- Target Distribution: A slight imbalance was observed, with 73 "No Disorder" cases versus 59 combined cases of Insomnia (n=29) and Sleep Apnea (n=30).
- Key Correlations: A strong positive correlation between Blood Pressure (Systolic/Diastolic) and Heart Rate with sleep disorders was confirmed.

### 🔬 Hypothesis Testing & Results (H1, H2 & H3)
Statistical tests and Logistic Regression models were used to validate the hypotheses, segmenting results by disorder type.

#### H1: Lifestyle and Physiological Factors

**H1a:** Obesity & Apnea ✅ Validated --> Apnea prevalence in the "Obese" group (57.14%) was significantly higher than in the "Normal" group (9.59%).
**H1b:** Stress & Insomnia✅ Validated --> Patients with Insomnia reported the highest average stress level (7.21).
**H1d:** Low Activity (<40 min)❌ Not Validated --> No significant difference in disorder prevalence was found between the low activity group (42%) and the adequate activity group (45%).
**H1e:** High HR / BP & Apnea ✅ Validated --> Elevated blood pressure and heart rate are significant indicators for Sleep Apnea risk.

#### H2: Age Effects
Age was established to have a moderate positive association with sleep disorders.
- Apnea vs. Insomnia: Sleep Apnea patients are consistently older (44.7 years) than Insomnia patients (41.6 years).
- Sleep Duration: The hypothesis that age correlates with lower sleep duration was rejected, with the opposite observed in this sample (positive correlation).

#### H3: Combined Risk Factor Model
An integrated risk scoring system for population segmentation was developed and strongly validated.

- Low Risk = 55% of population --> 18.31% disorder rate
- Medium Risk = 17% of population --> 62.50% disoreder rate
- High Risk = 28% of population --> 83.78% disorder rate

### 🏁 Conclusions & Insights
1. Predictive Efficacy: The combined risk model (H3) demonstrated a high capacity for population segmentation, showing a clear dose-response relationship (higher risk score equals higher disorder prevalence).
2. Disorder Differentiation: Risk factors are distinct: Insomnia is primarily associated with high stress levels and slightly younger ages; Sleep Apnea is strongly associated with high physiological metrics (BP, HR) and overweight/obesity.
3. Intervention Focus: The most effective preventive strategies should focus on blood pressure control and weight management to mitigate Apnea risk.