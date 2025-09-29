# **🎲 Board Games Analysis & Recommendation Engine**

## **Project Overview**

This project analyzes a **board games dataset** to uncover trends and build useful tools for players and enthusiasts.

* The data was **cleaned, organized, and stored in a SQL database** for efficient querying.

* A **filtering-based recommendation engine** (Python \+ Streamlit) helps users discover games based on:

  * Ratings

  * Playtime

  * Number of players

  * Complexity

* Visual charts highlight:

  * Top-rated games

  * Most-played games

  * Most-wishlisted games

Overall, this project combines **data engineering, analysis, and visualization** to deliver practical insights and personalized recommendations.

📑 **Presentation**: [Board Game Database](https://docs.google.com/presentation/d/1pBzKzOzYKCxy7n_QEZRLTVhZnCo_pdmCDucYisod0L8/edit?usp=sharing)

---

## **Data Sources**

* **Board Game CSV file**: Dataset with \~2000 rows

* **YAML configuration**: Used to dynamically manage file paths and input/output references

---

## **Figures**

* **ER Diagram**: A visual representation of the database logical structure

---

## **Libraries Used**

* pandas

* streamlit

* seaborn

* matplotlib

* PyYAML

---

## **Jupyter Notebooks**

### **`code_recommendation_engine.ipynb`**

* Load the database

* Drop irrelevant columns and clean `age` column

* Export cleaned database to CSV

* Build recommendation engine based on:

  * Minimum age

  * Number of players

  * Level of complexity

  * Playing time

* Order results by average rating

### **`code_for_graphs.ipynb`**

Exploratory Data Analysis (EDA) with visualizations:

* Top 10 most played games

* Top 10 trending/wishlisted games

* Top 10 rated games

* Correlation matrix

### **`importing_csv_sql.ipynb`**

* Create and import tables based on the ER diagram

---

## **SQL Scripts**

* **boardsgames\_schema\_V2.sql**: Defines table creation, primary keys, and foreign key relationships

* Data imported using the SQL Data Import Wizard

---

## **App**

* **app.py**: Contains the Streamlit app with the recommendation engine

Run locally with:

`streamlit run app.py`

---

## **How to Run the Project**

**Clone the repository**

 `git clone <repo_url>`

`cd <repo_name>`

**Create a virtual environment (recommended)**

 `python -m venv venv`

`source venv/bin/activate   # Mac/Linux`

`venv\Scripts\activate      # Windows`

**Install dependencies**

 `pip install -r requirements.txt`

**Run the Streamlit app**

 `streamlit run app.py`

Open the **localhost URL** in your browser to interact with the app.

---

## **Contributors**

Julia • Ricardo • Mauricio • Priyanka

