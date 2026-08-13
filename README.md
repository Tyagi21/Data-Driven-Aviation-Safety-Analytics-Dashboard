# ✈ Aviation Safety Analytics Dashboard

## Project Overview

The **Aviation Safety Analytics Dashboard** is a Data Science project developed during my internship at **VirtouStack Softwares Pvt. Ltd.** The project focuses on analyzing aviation operational data through data preprocessing, exploratory data analysis (EDA), and interactive dashboard visualization.

The dashboard provides meaningful insights into airline performance, airport operations, and flight delays using Python and Streamlit.

---

## Objectives

- Clean and preprocess aviation operational data.
- Perform Exploratory Data Analysis (EDA).
- Analyze airline and airport performance.
- Identify major causes of flight delays.
- Develop an interactive dashboard for aviation analytics.
- Present data-driven insights in an easy-to-understand format.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit

---

## Project Structure

```
Aviation_Safety_Dashboard/
│
├── app.py
├── data_preprocessing.py
├── eda_analysis.py
├── visualization.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── T_ONTIME_MARKETING.csv
│   └── aviation_cleaned.csv
│
├── screenshots/
│
└── reports/
```

---

## Dataset Information

- **Dataset:** U.S. Airline On-Time Performance Dataset
- **Original Size:** 696,049 Rows × 35 Columns
- **Processed Size:** 186,669 Rows × 21 Columns

The dataset was cleaned by:
- Removing missing values
- Removing duplicate records
- Removing unnecessary columns
- Handling outliers
- Preparing the data for analysis and visualization

---

## Dashboard Modules

### Home
- Dashboard overview
- Key Performance Indicators (KPIs)
- Total flights
- Airlines
- Airports
- Average departure delay
- Average arrival delay

### Dataset Overview
- Dataset preview
- Dataset dimensions

### Airline Analysis
- Airline-wise flight analysis
- Interactive airline selection
- Airline performance charts
- Average delay analysis

### Airport Analysis
- Airport-wise operational analysis
- Origin airport selection
- Top origin airports
- Top destination airports
- Destination city analysis

### Delay Analysis
- Delay statistics
- Delay cause distribution
- Delay comparison charts
- Highest delayed flights

### ℹ About
- Project details
- Technologies used

---

## Features

- Interactive dashboard
- Multi-page navigation
- Dynamic filters
- Interactive Plotly charts
- KPI cards
- Dark aviation-themed interface
- User-friendly visualization

---

## ▶ How to Run

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Start the Dashboard

```bash
streamlit run app.py
```

The dashboard will automatically open in your default web browser.

---

## Dashboard Preview

The dashboard includes:

- Home Dashboard
- Dataset Overview
- Airline Analysis
- Airport Analysis
- Delay Analysis

---

## Learning Outcomes

During this project, the following concepts were applied:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Dashboard Development
- Interactive Analytics using Streamlit
- Business Intelligence Dashboard Design

---

## Future Scope

The project can be further enhanced by:

- Integrating real-time flight data APIs
- Adding Machine Learning-based delay prediction
- Incorporating weather information
- Developing airport performance forecasting
- Deploying the dashboard on cloud platforms

---

## Developed By

**Arpit Tyagi**

B.Tech – Computer Science Engineering (Data Science)

Intern at **VirtouStack Softwares Pvt. Ltd.**
2026