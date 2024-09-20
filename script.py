import pandas as pd
import sqlite3
import os  # Para trabajar con nombres de archivos

# Conexión a SQLite (o crear una base de datos nueva)
conn = sqlite3.connect('database/data_sql/base_datos_instacart.db')
cursor = conn.cursor()

# Lista de archivos CSV
csv_files = ['database/data_csv/aisles.csv', 'database/data_csv/departments.csv', 'database/data_csv/instacart_orders.csv', 'database/data_csv/order_products.csv', 'database/data_csv/products.csv']

# Iterar por cada archivo CSV y cargarlo a SQL
for file in csv_files:
    # Leer archivo CSV
    df = pd.read_csv(file, sep=';')
    
    # Extraer el nombre del archivo sin la extensión
    table_name = os.path.splitext(os.path.basename(file))[0]  # Esto devuelve 'aisles', 'departments', etc.
    
    # Exportar el DataFrame a SQL
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    print(f'Datos del archivo {file} importados a la tabla {table_name}')

# Cerrar la conexión
conn.close()

