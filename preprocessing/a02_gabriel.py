import sys
import os
# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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

#1.Para cada hora del día, ¿cuántas personas hacen órdenes?

query='''
SELECT count(order_number) as count
FROM instacart_orders
GROUP BY order_hour_of_day
'''

ejemplo=pd.read_sql_query(query,conn)

print(ejemplo)


ejemplo.plot(title="Día de la semana la gente hace sus compras",
                        kind="bar",
                        xlabel="Hora del pedido",
                         ylabel="No.Personas que hacen pedido",
                         legend=False)
plt.show()



#7. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

query='''
SELECT order_count, COUNT(*) AS num_users
FROM (
    SELECT user_id, COUNT(order_id) AS order_count
    FROM instacart_orders
    GROUP BY user_id
) AS subquery
GROUP BY order_count
ORDER BY num_users DESC;

'''

ejemplo=pd.read_sql_query(query,conn)

print(ejemplo)


ejemplo.plot(title="Hora del pedido",
                        kind="bar",
                        xlabel="Pedidos",
                         ylabel="Clientes",
                         legend=False)
plt.show()


# 8. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

query='''
select product_name, count(o.product_id) as count_products

FROM [order_products] o 

JOIN [products] p ON o.product_id=p.product_id

Group by o.product_id

Order by count_products DESC

LIMIT 20

'''

ejemplo1=pd.read_sql_query(query,conn)

print(ejemplo1)


ejemplo1.plot(title="Hora del pedido",
                        kind="barh",
                        figsize=[15, 4],
                        x='product_name',
                        y='count_products',
                        xlabel="Pedidos",
                         ylabel="Clientes",
                         legend=False)
plt.show()
