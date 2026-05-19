# Customer Churn Analysis Dashboard

## Project Overview

This project focuses on analyzing customer churn behavior using Python, SQL, MySQL, and Power BI. The objective of the project is to identify patterns behind customer churn and generate actionable business insights using data analytics and visualization techniques.

The project includes data cleaning, exploratory data analysis (EDA), SQL-based business analysis, and an interactive Power BI dashboard for visual storytelling.

---

## Tech Stack

- Python
- Pandas
- NumPy
- SQL
- MySQL
- SQLAlchemy
- PyMySQL
- Power BI

---

## Project Workflow

## 1. Data Collection
- Imported customer churn dataset in CSV format.

## 2. Data Cleaning & Preprocessing
- Handled missing values
- Converted data types
- Removed inconsistencies
- Prepared dataset for analysis

## 3. Exploratory Data Analysis (EDA)
Performed analysis on:
- Churn distribution
- Monthly charges
- Contract types
- Customer tenure
- Payment methods

## 4. MySQL Integration
- Connected Python with MySQL
- Uploaded cleaned dataset into MySQL database
- Executed SQL queries for business insights

## 5. Power BI Dashboard
Built an interactive dashboard containing:
- KPI Cards
- Churn Distribution Pie Chart
- Contract Type vs Churn Analysis
- Monthly Charges Analysis
- Interactive Filters & Slicers

---

## Key Insights

- Customers with month-to-month contracts showed higher churn rates.
- Higher monthly charges were associated with increased churn probability.
- Long-term contract customers had better retention rates.
- Churn percentage analysis helped identify high-risk customer segments.

---

## Folder Structure

<pre>
Customer-Churn-Analysis/
│
├── data/
│   └── customer_churn.csv
│
├── output/
│   └── cleaned_churn_data.csv
│
├── scripts/
│   ├── churn_analysis.py
│   ├── churn_mysql_upload.py
│   └── sql_queries.sql
│
├── dashboard/
│   └── Customer_Churn_Dashboard.pbix
│
└── README.md
</pre>

### SQL Business Analysis Queries

Examples of SQL analysis performed:
<pre>
-- Total Customers
SELECT COUNT(*) FROM customer_churn;

-- Churn Distribution
SELECT Churn, COUNT(*) 
FROM customer_churn
GROUP BY Churn;

-- Average Monthly Charges
SELECT Churn, AVG(MonthlyCharges)
FROM customer_churn
GROUP BY Churn;
</pre>

### Power BI Dashboard
- Dashboard Features
- KPI Cards
- Churn Distribution
- Contract Analysis
- Monthly Charges Analysis
- Interactive Slicers

# Dashboard Preview

## Power BI Dashboard

![Power BI Dashboard](https://github.com/Ayushjssj/Sales-Data-Analysis-Dashboard/blob/f5946fdedb383fb6acfc2cacd4552d716f85ae53/output/Screenshot%202026-05-18%20192038.png)

---

## SQL Analysis Preview

![SQL Analysis](https://github.com/Ayushjssj/Sales-Data-Analysis-Dashboard/blob/main/output/Screenshot%202026-05-18%20192054.png?raw=true)

---

#### How to Run Project
<pre>
Step 1 — Install Required Libraries
pip install pandas numpy pymysql sqlalchemy
Step 2 — Run Python Analysis
python churn_analysis.py
Step 3 — Upload Data to MySQL
python churn_mysql_upload.py
Step 4 — Open Power BI Dashboard
Open:
Customer_Churn_Dashboard.pbix
</pre>

---

#### Future Improvements
- Machine Learning churn prediction
- Customer segmentation
- Advanced Power BI analytics
- Real-time dashboard integration

---

## Author
Ayush Pandey<br>
Aspiring Data Analyst & GenAI Enthusiast
- Python
- SQL
- MySQL
- Power BI
- Data Visualization
- Business Intelligence

### License 
This Project is licensed under the MIT License

---

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
