import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('database/data_sql/base_datos_instacart.db')

# 3. ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.


def respuesta_tres():
    query3 = '''
    SELECT days_since_prior_order, COUNT(*) AS recuento_pedidos
    FROM instacart_orders
    WHERE days_since_prior_order BETWEEN 1 AND 30
    GROUP BY days_since_prior_order
    ORDER BY days_since_prior_order ASC
    '''

    graf_3 = pd.read_sql_query(query3, conn)

    print(graf_3)

    graf_3.plot(title="Días desde la orden anterior",
                kind="bar",
                xlabel="Día del mes",
                ylabel="No. de pedidos",
                legend=False)

    plt.xticks(ticks=range(0, 30), labels=range(1, 31))
    plt.show()

# 4. Diferencia entre miércoles y sábados para `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# 7. ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?


def respuesta_siete():
    query7 = '''
    SELECT num_articulos, COUNT(*) AS num_pedidos
    FROM (
        SELECT order_id, COUNT(product_id) AS num_articulos
        FROM order_products
        GROUP BY order_id
    ) AS subquery
    GROUP BY num_articulos
    ORDER BY num_articulos
    '''
    graf_7 = pd.read_sql_query(query7, conn)
    print(graf_7)

    plt.figure(figsize=(10, 6))
    plt.bar(graf_7['num_articulos'], graf_7['num_pedidos'], color='skyblue')
    plt.title('Distribución del número de artículos por pedido')
    plt.xlabel('Número de artículos por pedido')
    plt.ylabel('Número de pedidos')
    plt.xticks(rotation=90)
    plt.grid(True)

    plt.show()


# 10. Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

def respuesta_diez():
    query10 = '''
    SELECT o.user_id, 
       SUM(CASE WHEN op.reordered = 1 THEN 1 ELSE 0 END) * 1.0 / COUNT(op.product_id) AS reorder_ratio
    FROM instacart_orders o
    JOIN order_products op ON o.order_id = op.order_id
    GROUP BY o.user_id;'''

    graf_10 = pd.read_sql_query(query10, conn)
    print(graf_10)

    sns.histplot(graf_10['reorder_ratio'], bins=30, kde=True)
    plt.title('Distribución de la Proporción de Productos Reordenados por Cliente')
    plt.xlabel('Proporción de Reordenes')
    plt.ylabel('Frecuencia')
    plt.show()


respuesta_tres()
respuesta_siete()
respuesta_diez()
