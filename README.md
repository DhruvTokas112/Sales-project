# Heading
### SubHeading
The dataset was taken from [kaggle](https://github.com/DhruvTokas112/Sales-project/blob/main/SQLquery.py).

---
Write Your Project discription here.
short bullet points
- point 1
- point 2

using star for bullet points
* point1
* point2

_The following code in [SQlquery.py](https://github.com/DhruvTokas112/Sales-project/blob/main/SQLquery.py) file is for reading the query and converting output to DataFrame_
```python
def read(query):
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)
    df.head()
    return df
```
