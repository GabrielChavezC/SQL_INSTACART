# Instacart

---

Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.

Tu misión es limpiar los datos y preparar un informe que brinde información sobre los hábitos de compra de los clientes de Instacart.

Diccionario de datos
Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.

- instacart_orders: cada fila corresponde a un pedido en la aplicación Instacart.

  - 'order_id': número de ID que identifica de manera única cada pedido.

  - 'user_id': número de ID que identifica de manera única la cuenta de cada cliente.

  - 'order_number': el número de veces que este cliente ha hecho un pedido.

  - 'order_dow': día de la semana en que se hizo un pedido (0 si es domingo).

  - 'order_hour_of_day': hora del día en que se hizo el pedido.

  - 'days_since_prior_order': número de días transcurridos desde que este cliente hizo su pedido anterior.

- products: cada fila corresponde a un producto único que pueden comprar los clientes.

  - 'product_id': número ID que identifica de manera única cada producto.

  - 'product_name': nombre del producto.

  - 'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.

  - 'department_id': número ID que identifica de manera única cada departamento de víveres.

- order_products: cada fila corresponde a un artículo pedido en un pedido.

  - 'order_id': número de ID que identifica de manera única cada pedido.

  - 'product_id': número ID que identifica de manera única cada producto.

  - 'add_to_cart_order': el orden secuencial en el que se añadió cada artículo en el carrito.

  - 'reordered': 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.

- aisles

  - 'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.

  - 'aisle': nombre del pasillo.

- departments

  - 'department_id': número ID que identifica de manera única cada departamento de víveres.

  - 'department': nombre del departamento.

# Resolver las siguientes preguntas

---

1. Para cada hora del día, ¿cuántas personas hacen órdenes? Gabriel ✅

2. ¿Qué día de la semana compran víveres las personas? Ruben ✅

3. ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos. Carol ✅

4. Diferencia entre miércoles y sábados para `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas. (pendiente)

5. ¿Cuál es la distribución para el número de pedidos por cliente? Ruben✅

6. ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)? Rosa ❌

7. ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución? Carol ✅

8. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)? Gabriel ✅

9. Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir? Ruben ❌

10. Para cada cliente, ¿qué proporción de sus productos ya los había pedido? Carol ✅

11. ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos? Rosa ❌
