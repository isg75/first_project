# 🌍 Vanguard A/B Testing: Website Redesign Performance Analysis

## Objective
This project uses A/B testing to evaluate the performance of a new website design compared to the existing version. Our goal is to determine — through formal statistical hypothesis testing — whether the new design improves key user behavior metrics, such as completion rate and time efficiency. In addition, we aim to uncover potential usability issue(s) within the new design for further refinement.

---

## 🔍 Hypothesis

We hypothesize that the new website design improves user performance across several key indicators, including:

### A higher completion rate

### Lower error (reversal) rates

### Shorter time spent on steps, indicating better usability

We will apply statistical hypothesis testing (2 Sample T-tests) to compare performance metrics between users assigned to the old design (control group) and the new design (test group).

---

## Funnel Structure
The user journey consists of three sequential steps, followed by a final "Confirm" step, representing successful completion. Users may proceed forward or move backward in the process. Backward navigation (step reversal) may indicate confusion or design inefficiencies.

This funnel structure provides the framework for defining and analyzing all metrics.

---

## Primary Metric
- Quality Visits Leading to Confirmation

A "quality visit" is defined as a session in which the user completes all steps and reaches the final "Confirm" stage.
  
### KPIs

#### Key Performance Indicators (KPIs)

Each KPI below was subjected to hypothesis testing to assess whether the differences between the old and new designs are statistically significant.

##### Completion Rate without error regardless of prior error visits
The proportion of users who reach the final "Confirm" step in one visit. Comparing the test group +5% threshold (cost-effectiveness)
Hypothesis test: Z-test

##### Time Spent on Each Step
The average time users spend at each step of the funnel, analyzed by age group.
Hypothesis test: T-Test

##### Error Rate (Step Reversals)
Proportion of users (according to age group)  who move backward in the process flow (from a later step to an earlier one) and fail to complete the final step – control and test group separation.
Hypothesis test: T-Test

#### Age Group Engagement
Comparison of the average session duration (in seconds) across defined age groups (<30, 30–39, 40–49, 50-59, 60-69, 70-79, 80+) between control group and test group of the website.
Test: Barplot

#### Expected Outcomes
- Statistically confirm whether the new design improves user engagement and conversion.
- Ensure that engagement remains consistent across age groups.
- Identify steps in the funnel where users experience friction (e.g., high reversal rates or time delays) and provide actionable redesign suggestions.


## 🧾 Dataset Description

### 🧱 Raw Datasets:

- **df_final_demo.txt**
- **df_final_experiment_clients.txt**
- **df_final_web_data_pt_1.txt**
- **df_final_web_data_pt_2.txt**

### Dataset obstacles:
- 
- **df_final_experiment_clients.txt**
- ~ 20,000 rows were deleted due to multiple NaN values
  
- **df_final_demo.txt**
- 14 rows were delted due to all columns having Nan values

### Final 
> Note: All txt file were individually exported to single csv files.  After cleaning, individual csv files were exported to be merged into one table. This made querying easier.
- **merged_df_clean.csv**

---

## 💻 Technologies Used

| Area                 | Tools/Technologies                                      |
|----------------------|---------------------------------------------------------|
| Data Manipulation    | Python (Pandas, NumPy)                                  |
| Data Visualization   | Matplotlib, Seaborn, Pyplot                             |
| Documentation        | Jupyter Notebook, Markdown, GitHub,                     |
| Version Control      | Git, GitHub, Anaconda Powershell                        |
| Statistical Analysis | Scipy, statsmodels                                      |


---

## 📦 Deliverables

- ✅ [Repository "vanguard-ab-test" on GitHub](https://github.com/Brenvillag/vanguard-ab-test) 
- ✅ [Raw dataset](https://github.com/data-bootcamp-v4/lessons/tree/main/5_6_eda_inf_stats_tableau/project/files_for_project)
- ✅ Jupyter Notebook with cleaned and documented dataset (`merged_df_clean.csv`)
- ✅ Jupyter Notebook calling of the functions 
- ✅ Python ".py"-file with functions
- ✅ Tableau file
- ✅ [Group 1 Trello Project Page](https://trello.com/b/xIrQ1kK7/vanguard-ab-test)
- ✅ README documentation: README.md
- ✅ [Group 1 Presentation](https://docs.google.com/presentation/d/1Z9yE8gTMzNdZwtDIAucWzqTXzSzvAsn52Qk6IsR0oF4/edit?usp=sharing) 


---

## 👨‍💼 Target Audience

- **Target Market**: AGE GROUP - We have to cater to the older clients to "confirm"
- **Stakeholders**: Suggest changes or accept the new design
- **Analysts / Webdesigners**: Offer a clean dataset for further projects or optimizations

---

## 🛠️ Future Work
- **Assist in Webdesign optimizations**: Notebooks and function python file ready to use after later changes

---

## 👥 Contributors

- Brenda Villaverde
- Damian Witkowski
- Sherin Kuruvilla
- Delmar Bumanglag

---

## 🌐 We have proven our hypthesis
### WE NEED TO CHANGE THIS 
📢 *The web design does contribute to a faster confirm rate per visit.*


