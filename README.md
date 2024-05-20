# SWIFT MARKET DATASET ANALYSIS

The [dataset](https://github.com/DhruvTokas112/Sales-project/blob/main/SwiftMarket-data.sql)

---
OVERVIEW

This project involves a comprehensive analysis of the SWIFT market dataset. The aim is to uncover insights and trends within the data, providing a deeper understanding of the market dynamics captured by SWIFT transactions.

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
![Grocery](https://5.imimg.com/data5/KQ/LQ/VE/SELLER-14757215/shopping-mall-construction.jpg)

| column1 | column 2|
|---------|---------|
| value1  | value 2 |
| vaue 3  | value 4 |


