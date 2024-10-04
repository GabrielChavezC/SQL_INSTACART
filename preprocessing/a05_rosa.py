
import sys
import os
# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import pandas as pd 
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

cursor = conn.cursor()  
cursor.execute(query_6)    
results = cursor.fetchall() 

for row in results:
    print(f"ID: {row[0]}, Producto: {row[1]}, Cantidad: {row[2]}")

# 11.¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

query_11 = '''
SELECT p.product_name, COUNT(o.product_id) AS add_to_cart_order
FROM order_products o
JOIN products p ON o.product_id = p.product_id
GROUP BY o.product_id
ORDER BY add_to_cart_order DESC
LIMIT 20
'''
cursor = conn.cursor()  # Crear un cursor para ejecutar la consulta
cursor.execute(query_11)    # Ejecutar la consulta
results = cursor.fetchall()  # Obtener todos los resultados

for row in results:
    print(f"Producto: {row[0]}")

# 4. Diferencia entre miércoles y sábados para 'order_hour_of_day'. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# Consulta SQL
query_4 ='''
SELECT  o.order_hour_of_day) AS order_hour_of_day
COUNT(o.order_id) AS order_count,
        (o.order_dow) AS day_of_week
FROM order_products o
WHERE order_dow IN ('3', '6')  -- 3 es miércoles, 6 es sábado
GROUP BY order_hour_of_day, order_dow
ORDER BY order_hour_of_day
'''

graf_4 = pd.read_sql_query(query_4, conn)
print(graf_4)

# Ejecutar la consulta
cursor = conn.cursor()
cursor.execute(query_4)

# Cargar los resultados en un DataFrame
data = cursor.fetchall()
df = pd.DataFrame(data, columns=['order_hour_of_day', 'order_count', 'order_dow'])

# Convertir 'order_dow' a un nombre legible
df['day_of_week'] = df['order_dow'].replace({'3': 'Wednesday', '6': 'Saturday'})
df['order_hour_of_day'] = df['order_hour_of_day'].astype(int)  # Convertir a int



# Gráfico de barras
graf_4.plt.figure(figsize=(12, 6))
for day in df['day_of_week'].unique():
    subset = df[df['day_of_week'] == day]
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
