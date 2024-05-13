import os
from dotenv import load_dotenv
import mysql.connector
#from my sql import connector
import pandas as pd
 
load_dotenv()

host=os.getenv('HOST')
user=os.getenv('USER')
password=os.getenv('PASSWORD')

database='swiftmarket'

connection = mysql.connector.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database)
cursor = connection.cursor()
 
def read(query):
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)
    df.head()
    return df

def show_tables():
    query="""SHOW TABLES;"""
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)
    df.head()