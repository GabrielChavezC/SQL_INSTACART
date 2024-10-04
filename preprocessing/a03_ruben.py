import sys
import os
# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 

#2. ¿Qué día de la semana compran víveres las personas?
conn=sqlite3.connect('database/data_sql/base_datos_instacart.db')
consulta_2='''
SELECT COUNT(order_number), order_dow
FROM instacart_orders
GROUP BY order_dow


'''

query_2=pd.read_sql_query(consulta_2,conn)

print(query_2)

query_2.plot(title="Día de la semana la gente hace sus compras",
                        kind="bar",
                        xlabel="Dia de la semana",
                         ylabel="No.Personas que hacen pedido",
                         legend=False)
plt.show()


# 5. ¿Cuál es la distribución para el número de pedidos por cliente?

consulta_5 ='''
SELECT total_pedidos, COUNT(*) as Total_de_Clientes
FROM (
SELECT user_id, COUNT(*) as total_pedidos
FROM instacart_orders
GROUP BY user_id
) AS subconsulta
GROUP BY total_pedidos

'''
query_5=pd.read_sql_query(consulta_5,conn)
print(query_5)

query_5.plot(title="Distribución para el número de pedidos por total de clientes",
                        kind="bar",
                        xlabel="Nº de Pedidos",
                         ylabel="Nº.Personas que hacen pedido",
                         legend=False,
                         grid=True)
plt.show()

# 9. Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# 4. Diferencia entre miércoles y sábados para `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.