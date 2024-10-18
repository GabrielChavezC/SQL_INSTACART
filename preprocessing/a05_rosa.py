
import sys
import os
# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import pandas as pd 
import seaborn as sbn
import matplotlib.pyplot as plt 


conn = sqlite3.connect('database/data_sql/base_datos_instacart.db')

# 6. ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?
query_6 ='''
SELECT p.product_id, p.product_name, COUNT(o.product_id) AS count_products
FROM order_products o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY count_products DESC
LIMIT 20
'''
graf_6 = pd.read_sql_query(query_6, conn)
print(graf_6)

#Graficando el resultado de la consulta
plt.figure(figsize=(10, 6))

# Crear la gráfica de barras con Matplotlib
plt.barh(graf_6['product_name'], graf_6['count_products'], color='skyblue')

# Añadir títulos y etiquetas
plt.title('Top 20 productos más populares', fontsize=16)
plt.xlabel('Número de productos vendidos')
plt.ylabel('Nombre del producto')

# Invertir el orden del eje y para que el producto más vendido esté arriba
plt.gca().invert_yaxis()

# Mostrar la gráfica
plt.tight_layout()
plt.show()

#los articulos mas populares son las Bananas, son los que mas sobresalen de los 20 mas populares

# 11.¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

query_11 = '''
SELECT p.product_name, COUNT(o.product_id) AS count_first_added
FROM order_products o
JOIN products p ON o.product_id = p.product_id
WHERE o.add_to_cart_order = 1
GROUP BY o.product_id, p.product_name
ORDER BY count_first_added DESC
LIMIT 20;
'''
graf_11 = pd.read_sql_query(query_11, conn)
print(graf_11)

#Graficando el resultado de la consulta
plt.figure(figsize=(10, 6))

# Crear la gráfica de barras con Matplotlib
plt.barh(graf_11['product_name'], graf_11['count_first_added'], color='skyblue')

# Añadir títulos y etiquetas
plt.title('Top 20 productos elegidos en primer lugar', fontsize=16)
plt.xlabel('Número de veces añadido al carrito')
plt.ylabel('Nombre del producto')

# Invertir el orden del eje y para que el producto más vendido esté arriba
plt.gca().invert_yaxis()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
#Nuevamente las Bananas son los productos que los clientes ponen primero en su carrito, los productos organicos tambien destacan.

# 4. Diferencia entre miércoles y sábados para 'order_hour_of_day'. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# Consulta SQL
query_4 ='''
SELECT o.order_hour_of_day AS order_hour_of_day,
       COUNT(o.order_id) AS order_count,
       o.order_dow AS day_of_week
FROM order_products 
WHERE o.order_dow IN ('3', '6')  -- 3 es miércoles, 6 es sábado
GROUP BY o.order_hour_of_day, o.order_dow
ORDER BY o.order_hour_of_day;
'''

graf_4 = pd.read_sql_query(query_4, conn)
print(graf_4)


# Convertir 'order_dow' a un nombre legible
graf_4['day_of_week'] = graf_4['order_dow'].replace({'3': 'Wednesday', '6': 'Saturday'})
graf_4['order_hour_of_day'] = graf_4['order_hour_of_day'].astype(int)  # Convertir a int



# Gráfico de barras
graf_4.plt.figure(figsize=(12, 6))
for day in graf_4['day_of_week'].unique():
    subset = graf_4[graf_4['day_of_week'] == day]
    plt.bar(subset['order_hour_of_day'] + (0.2 if day == 'Wednesday' else -0.2), 
            subset['order_count'], 
            width=0.4, 
            label=day)

plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.title('Orders per Hour: Wednesday vs Saturday')
plt.xticks(range(24))  # Asegúrate de que todas las horas estén representadas
plt.legend()
plt.grid()
plt.show()
