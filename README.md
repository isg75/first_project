# **Berlin Marathon Project**

## **Introduction**
The Berlin Marathon is one of the world’s most prestigious long-distance running events, known for its fast course and record-breaking performances.  

For this project, we positioned ourselves as a **data analytics company** hired by a **sports magazine** to analyze the Berlin Marathon’s history.  
The goal is to provide insights that will support the magazine in writing a feature article about the marathon, focusing on performance trends, gender dynamics, country dominance, and female participation.  

Throughout this project, we applied data wrangling, cleaning, and exploratory data analysis (EDA) techniques to answer key research questions and test hypotheses about the evolution of the Berlin Marathon.

---

## **Datasets**
We used **two datasets**, both of which were cleaned and transformed before analysis:

### **1. Berlin Marathon Runners Dataset (1974–2024)**  
- Source: [Kaggle – Berlin Marathons Data](https://www.kaggle.com/datasets/aiaiaidavid/berlin-marathons-data)  
- Shape after cleaning: ~884,000 rows, 5 columns (`year`, `gender`, `time`, `finish_time`, `finish_seconds`).  
- Strengths: Covers all participants, allows analysis of participation and performance distributions.  
- Weaknesses: Missing country data for many runners.

### **2. Berlin Marathon Winners Dataset (1974–2024)**  
- Source: [Wikipedia – Berlin Marathon](https://en.wikipedia.org/w/index.php?title=Berlin_Marathon&action=edit)  
- Shape after cleaning: 100 rows, 5 columns (`year`, `winner`, `country`, `time`, `gender`).  
- Strengths: Clean overview of winners per year, good for studying records and country dominance.  
- Weaknesses: Only includes winners, does not represent the full participant population.

---

## **Research Questions**

### **1. Evolution of performance (Rafael)**  
- How have winning times evolved in the Berlin Marathon from 1974 to 2024?  
- Are world records being broken more frequently in Berlin than in other marathons?  

### **2. Gender time scores difference 
of female and male winner (Kinga)**  
- What is the time difference between male and female winners?  
- Has the gender time scores difference decreased over the years? 


### **3. Country dominance (Irma)**  
- Which countries have produced the most winners in the Berlin Marathon?  
- How has the country distribution of winners shifted across decades?  

### **4. Female participation (Joma)**  
- How has the percentage of female runners changed since 1974?  
- Is the finishing time distribution of female runners approaching that of male runners?  

---

## **Hypotheses**
1. Winning times in the Berlin Marathon have significantly improved over the years.  
2. The time score difference between men and women has decreased over time.  
3. The number of participants from Africa has increased over the years.  
4. Female participation has increased since 1974.  

---

## **Methodology**
We applied multiple **data cleaning and wrangling techniques** to both datasets:

- Standardized column names to `snake_case`.  
- Removed duplicates and irrelevant columns (`country`, `age` in the raw runners dataset).  
- Handled missing values (nulos in `country`, `age`).  
- Normalized categorical values (`gender`: male/female/unknown).  
- Converted `time` to `timedelta` and created `finish_seconds`.  
- Reshaped winners dataset (wide → long format) and added `gender` column.  
- Saved final cleaned datasets to `data/clean/`.

For analysis, we used:  
- **Aggregation & filtering** with `groupby`, `value_counts`, and pivot tables.  
- **Visualizations** with Matplotlib and Seaborn.  
- Exported figures to `figures/` for presentation.  

---

## **Results & Insights**

### **1. Evolution of performance (Rafael)**  
- Winning times in the Berlin Marathon have consistently improved.  
- Men’s performances have stabilized just above **2h01**.  
- Women achieved a major breakthrough in **2023 with 2h11**.  
- Berlin is the **leading marathon for world records**, hosting nearly all men’s records since 2003 and the women’s record in 2023.  
- This far surpasses other cities like London or Chicago.

### **2. Gender time scores difference (Kinga)**  
- Time results changed over the years for both genders.  
- The gender time scores difference has decreased.  


### **3. Country dominance (Irma)**  
- **Kenya (25 wins)** and **Ethiopia (20 wins)** dominate the overall history.  
- In early decades, winners came mainly from Europe (West Germany, UK).  
- Since the 1990s, East African countries have taken the lead.  

### **4. Female participation (Joma)**  
- Female participation has increased explosively since 1974 (5.0%). There has been a average 40% increase in female participation.In 2024: there is a 45% increase.
- Time gap between finishing times for female runners and male runners is steadily decreasing. In 1974, the time gap was at 61.3 min. As of 20204,  it is now at a 30.4 min difference.  At this current rate, times will be equal in 49 years

---

## **Conclusions**
- **Hypothesis 1:** Supported – Winning times have consistently improved; men are near the 2h01 barrier and women set a breakthrough with 2h11 in 2023. Berlin is confirmed as the fastest course, with nearly all world records since 2003.  
- **Hypothesis 2:** Supported – The performance gap score between men and women has narrowed.  
- **Hypothesis 3:** Supported – African participation and victories have grown strongly (Kenya and Ethiopia lead since the 1990s).  
- **Hypothesis 4:** Supported – Female participation has risen steadily since 1974.  

---

## **Future Questions**
- How do Berlin results compare to other World Marathon Majors (London, Boston, Tokyo)?  
- What external factors (weather, temperature, technology, shoes) influence performance trends?  
- How do amateur vs. elite trends differ?  

---

## **Project Organization**

### 📂 Repository Structure
first_project/
├── 📂 data
│ ├── 📂 raw
│ └── 📂 clean
│
├── 📂 figures
├── 📂 notebooks
├── 📂 slides
├── 📂 sql_scripts

├── 📄 config.yaml
├── 📄 main.py
├── 📄 pyproject.toml
├── 📄 README.md
└── 📄 uv.lock

---

## **Teamwork**
- Project managed with **Trello**: [Berlin Marathon Project Trello](https://trello.com/invite/b/68d3cd5c7e316c4e2b2dd967/ATTI582c762f1ce0f9a2b5cf205744fc802d5600E419/berlin-marathon-data-analysis-project)  
- GitHub collaboration with branches per member (Irma, Kinga, Rafael, Joma).  
- Each member responsible for one research question.  

---

## **Deliverables**
- Cleaned datasets in `/data/clean/`.  
- Analysis notebooks in `/notebooks/`.  
- Figures in `/figures/`.  
- Final presentation: [Google Slides](https://docs.google.com/presentation/d/1ppWy2WtMmzKg47Q6yj-O25uKoOPrUDnsZRDllIabRcA/edit?usp=sharing)  

---

## **Authors**
- Rafael – Analysis of Evolution of performance  
- Kinga – Analysis of Gender gap  
- Irma – Analysis of Country dominance  
- Joma (Project Manager) – Analysis of Female participation  
