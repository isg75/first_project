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

