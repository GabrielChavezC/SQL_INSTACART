import sys
import os
# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 

#1. Para cada hora del día, ¿cuántas personas hacen órdenes?
conn=sqlite3.connect('database/data_sql/base_datos_instacart.db')
query='''
SELECT count(order_number) as count
FROM instacart_orders
GROUP BY order_dow
'''

ejemplo=pd.read_sql_query(query,conn)

print(ejemplo)


ejemplo.plot(title="Día de la semana la gente hace sus compras",
                        kind="bar",
                        xlabel="Dia de la semana",
                         ylabel="No.Personas que hacen pedido",
                         legend=False)
plt.show()


#=======================================================================================================================
                                                       #Gabriel 
#=======================================================================================================================











#=======================================================================================================================
                                                       #Ruben 
#=======================================================================================================================









#=======================================================================================================================
                                                       #CARO
#=======================================================================================================================
