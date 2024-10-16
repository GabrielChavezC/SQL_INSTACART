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


def respuesta_cuatro():
    query4 = '''
    SELECT order_dow, order_hour_of_day, COUNT(order_id) AS total_pedidos
    FROM instacart_orders
    WHERE order_dow = 3 or order_dow = 6
    GROUP BY order_dow, order_hour_of_day
    ORDER BY order_dow, order_hour_of_day;
    '''
    graf4 = pd.read_sql_query(query4, conn)
    print(graf4)

    # Acomodar los datos para una mejor gráfica
    graf4_pivot = graf4.pivot(
        index='order_hour_of_day', columns='order_dow', values='total_pedidos')

    ax = graf4_pivot.plot(kind='bar',
                          figsize=(10, 6),
                          title="Comparación de pedidos entre Miércoles y Sábados por hora del día",
                          xlabel="Hora del día",
                          ylabel="Número de pedidos",
                          legend=False)

    ax.legend(['Miércoles', 'Sábado'])
    plt.show()


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

    # Conocer el limite del 3er cuartil para delimitar el siguien gráfico
    sns.boxplot(x=graf_7['num_articulos'])

    plt.title('Distribución del número de artículos por pedido')
    plt.xlabel('Número de artículos por pedido')

    plt.show()

    # Se realiza el gráfico hasta el número aproximado del 3er cuartil, el 75% de los datos
    graf_7_filtrado = graf_7[graf_7['num_articulos'] <= 70]

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(graf_7_filtrado['num_articulos'],
            graf_7_filtrado['num_pedidos'])
    plt.title('Distribución del número de artículos por pedido (hasta 70)')
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
respuesta_cuatro()
