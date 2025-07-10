# Project overview

This project explores the Global AI job Market and Mental health Issues relational databases and SQL, to create a specialized consulting service that helps individuals enter the data job market. This service combines:
Job market analysis using data-driven insights into job roles, salaries, experience levels, education, and regions.
Mental health and wellness advice for remote workers.
This end-to-end project involves data modeling, database creation, SQL querying, insight generation, and Python-based data visualization.

- 🛠 GitHub Repository: [fist_project](https://github.com/MiguelSoares1/first_project)
- 📋 Trello Board: [Project Tasks & Timeline](https://trello.com/b/vZzROWNR/global-ai-job-market-trends-salary)
- 🖼 ERD Diagram: [erd/ai_job_ERD.png](https://drawsql.app/teams/ironhack-34/diagrams/ai-job-dataset) and [health_impact_ERD.png](https://drawsql.app/teams/ironhack-34/diagrams/health-impact)
- Presentation: [ Global AI job market ](https://docs.google.com/presentation/d/10C4iM9QNUbr2kSS1-GjYP2EgXsZBRndRMB3xpewEJeg/edit?slide=id.g36e20e69003_0_5#slide=id.g36e20e69003_0_5)

---


# Questions 

**Business Problem & Hypothesis**

>Business Case: AI Career Consultant – Career and Wellness Consulting for the AI Job Market


**Problem**
> Many aspiring AI professionals lack clarity on where to start: what roles exist, required skills, realistic salaries, and career paths.
Remote work—common in tech and AI—has significant impacts on mental health, including stress, burnout, and isolation, especially for early-career professionals. 

**Hypothesis**
> 1. Professionals face significant barriers when trying to access AI roles. The roles ask for a variety of different skills and experience.
> 2. Professionals in AI roles with greater responsibility and high salary expectations face higher levels of stress and emotional exhaustion, especially in more senior roles.



# Dataset 


| Dataset Name                                          | Description |
|-------------------------------------------------------|-------------|
| `Global AI Job Market Trends & Salary Insights 2025 ` | Explore AI job roles, salaries, skills demand, and remote work trends worldwide |
| `Remote Work Of Health The Post-Pandemic`             | The dataset presents a comprehensive, global snapshot of how remote, hybrid, and onsite work arrangements are influencing the mental and physical health of employees in the post-pandemic era. |


## Main dataset issues

- The data collected by Global AI Job Market Trends & Salary Insights 2025
-The DB provided by 'The data collected by Global AI Job Market Trends & Salary Insights 2025' was giving information about jobs, including three separate columns for skills associated with each job. 


## Solutions for the dataset issues
- To properly normalize the data and hand the many-to-many relationship between jobs and skills, it was necessary to create a bridge table linking jobs to individual skills.

# Insights 
-High salaries correlate with advance degrees + experience
-Mental health issues increase with remote job intensity, specially with job-office work.
-Certain regions show faster AI job growth.
-Some certifications are more valuable than others.


# Conclusions and next steps

AI Job Market Insights
- Data shows a strong correlation between higher salaries and advanced degrees or specialized skills (e.g., Python, SQL, cloud platforms).
- Remote work is growing, but it comes with increased mental health risks like burnout and isolation.


Mental Health Findings
-Professionals in high-pressure, remote AI jobs report greater stress and work-life imbalance.
-Preventive strategies (breaks, wellness programs, flexible hours) can improve productivity and morale.

Data-Driven Consulting Value
-An integrated approach that combines career insights with mental health advice can guide individuals more holistically.
-This positions the consulting service as not just job-oriented, but human-centered.

# Repository Structure

```

first_project/
├── data/                        # Raw and cleaned CSV files
├── fugires/                     # Grafics
├── sql/                         # SQL scripts and queries
├── notebooks/                   # Python notebooks with analysis
├── slides/                      # Presentation
├── README.md                    # Introduction of the purpose of this project
├── .gitignore                   # 
├── requirements.txt             # List of libraries and versions used 
└── requirements-dev.txt         # List of libraries and versions used, without Jupyter

```


##  Tools Used

- MySQL  
- Python (Pandas, Seaborn, Matplotlib)  
- Jupyter Notebooks  
- Git & GitHub  
- Trello (for task planning)  
- Draw.io (for ERD)
- Visual Studio Code IDE & plugins
  
---

## 👥 Team Members

__*Guilherme Haas
Macarena Ruiz
Miguel Soares
Sumaiya Parvin*__