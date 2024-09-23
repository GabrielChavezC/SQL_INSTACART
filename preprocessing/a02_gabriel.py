import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
from functions.funciones_udf import cubo 

conn=sqlite3.connect('database/data_sql/base_datos_instacart.db')


# Esta función se puede utilizar en consultas SQL dentro de esta conexión
conn.create_function('cubo1', 1, cubo)

query='''
SELECT *,cubo1(add_to_cart_order) as CUBO
from order_products
LIMIT 10
'''

ejemplo=pd.read_sql_query(query,conn)

print(ejemplo)
