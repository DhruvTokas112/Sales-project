# SWIFT MARKET DATASET ANALYSIS

---

This project provides an in-depth analysis of the SWIFT market dataset, focusing on various aspects of sales performance, trends, and employee contributions. The analysis aims to uncover patterns, identify top performers, and provide actionable insights through data-driven methodologies.


The [dataset](https://github.com/DhruvTokas112/Sales-project/blob/main/SwiftMarket-data.sql)


Write Your Project discription here.
short bullet points
- point 1
- point 2

using star for bullet points
* point1
* point2


Analysis and Findings:
* Annual Sales Performance Visualization
* Monthly Sales Trend Analysis Using Moving Average
* Month-over-Month Sales Growth Rate
* Top-Performing Sales Representatives
* Total Sales by Employee
* Highest Sales Category
* Customer Distribution by State
* Average Quantity of Each Product Sold
* Top Supplier by Sales
* Total Revenue by State
* Sales by Customer
* Total Salary Expenditure by Department
* Subcategory with Highest Average Unit Price
* Total Revenue by Category


Tools and Technologies
* Programming Languages: Python
* Libraries: pandas, NumPy, Matplotlib, Seaborn
* Platforms: Jupyter Notebook for interactive data analysis and visualization


_The following code in [SQlquery.py](https://github.com/DhruvTokas112/Sales-project/blob/main/SQLquery.py) file is for reading the query and converting output to DataFrame_
```python
def read(query):
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)
    df.head()
    return df
```
***

| column1 | column 2|
|---------|---------|
| value1  | value 2 |
| vaue 3  | value 4 |


