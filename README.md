# Retail Sales Data Analysis Using Python

## 📌 Project Overview

This project uses Python to analyze retail sales data and identify patterns in revenue, product performance, and regional sales.

The goal is to transform raw sales data into meaningful business insights that can help organizations understand their performance and make data-driven decisions.

This is a beginner-friendly data analytics project created to demonstrate practical skills in Python, data cleaning, exploratory data analysis (EDA), and data visualization.

**Dataset:** Synthetic retail sales data created for learning and portfolio purposes.

## 🎯 Business Objectives

This project explores five key business questions:

1. What is the total revenue generated?
2. Which product categories generate the most revenue?
3. Which products contribute the most to sales?
4. How does revenue change month by month?
5. Which regions generate the most revenue?

## 🛠️ Tools and Technologies

- **Python** — Data analysis and calculations
- **Pandas** — Data manipulation, cleaning, and aggregation
- **Matplotlib** — Data visualization
- **CSV** — Data storage and reporting
- **GitHub** — Project documentation and version control

## 📂 Project Structure

```text
retail-sales-python-project/
│
├── retail_sales.csv
│
├── outputs/
│   ├── revenue_by_category.png
│   ├── monthly_revenue.png
│   ├── revenue_by_region.png
│   ├── revenue_by_category.csv
│   ├── revenue_by_product.csv
│   ├── monthly_revenue.csv
│   └── revenue_by_region.csv
│
├── analysis.py

## 🧹 Data Cleaning and Preparation

The Python script performs several data preparation steps:

- Converts order dates into datetime format.
- Converts quantity, unit price, and discount columns into numeric values.
- Removes duplicate order IDs.
- Removes records missing essential information.
- Filters invalid quantities and prices.
- Handles missing discount values.
- Calculates gross sales and revenue after discounts.
- Creates a month column for monthly trend analysis.

## 📊 Analysis and Visualizations

### 1. Revenue by Product Category

Compares revenue across product categories to identify which categories contribute the most to overall sales.

### 2. Top Products by Revenue

Ranks products by revenue to highlight the products generating the most sales.

### 3. Monthly Revenue Trends

Analyzes monthly revenue to identify changes in sales performance over time.

### 4. Revenue by Region

Compares revenue across regions to understand differences in regional performance.

The script generates three charts and exports four summary tables to the `outputs/` folder.

## 📈 Key Performance Indicators

The project calculates the following business metrics:

| Metric | Description |
|---|---|
| Total Revenue | Revenue after discounts |
| Total Units Sold | Total quantity of products sold |
| Total Orders | Number of unique order IDs |
| Average Revenue per Order | Total revenue divided by unique orders |

## 💻 How to Run This Project

### Step 1: Download the Repository

Download or clone the project to your computer.

### Step 2: Install Dependencies

Open a terminal in the project folder and run:

```bash
py -m pip install -r requirements.txt
```

### Step 3: Execute the Python Script

Run the following command:

```bash
py analysis.py
```

### Step 4: Review the Results

- Review the sales summary printed in the terminal.
- Open the `outputs/` folder to view the generated charts.
- Open the CSV summary files in Excel or another data analysis tool.

## 💡 Business Applications

This type of analysis can help businesses:

- Compare product and category performance.
- Monitor revenue trends over time.
- Identify regional differences in sales.
- Determine where additional investigation may be useful.
- Support decisions using summarized data.

## 🚀 Future Enhancements

Planned improvements include:

- Integrating SQL queries using SQLite.
- Building an interactive Power BI dashboard.
- Adding product costs to analyze profitability.
- Performing statistical analysis of sales trends.
- Exploring machine learning for sales forecasting.

## 📚 Skills Demonstrated

Python | Pandas | Data Cleaning | Exploratory Data Analysis | Data Visualization | KPI Calculation | Business Analysis

## 👩‍💻 Author

Aspiring Data Analyst / Data Science Associate

This project demonstrates my practical application of Python to data analysis and my commitment to developing skills in data-driven decision-making.

