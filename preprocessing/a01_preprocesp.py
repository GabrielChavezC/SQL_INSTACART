import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 


conn=sqlite3.connect('database/data_sql/base_datos_instacart.db')
query='''
SELECT * from aisles
'''

ejemplo=pd.read_sql_query(query,conn)

print(ejemplo)