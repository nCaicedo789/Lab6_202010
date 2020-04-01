Nicolas Caicedo Murgueitio 201820789
Vytis Karanauskas 201912961

REFLEXIÓN

8.5 - Complementar las pruebas unitarias del RBT para 3 funciones adicionales, incluyendo valueRange.

El documento con la reflexión respecto a la complejidad temporal teórica y el tiempo promedio obtenido en las operaciones realizadas. Debe también discutir y comparar la complejidad de la consulta del requerimiento 3 con respecto al requerimiento 2 del reto 3. 

Comparando los laboratorios del requerimiento y el 3 podemos ver que hay una notable diferencia entre los tiempos de carga de los datos. En ambos casos se usa el archivo pequeño de datos.
En el Lab5 el tiempo promedio es de 0.08 segundos mientras que en el Lab6 el tiempo promedio es de 0.13 segundos. Esto puede deberse a la complejidad y profundidad de los mapas que se están generando.
Al modificar el controller para generar solo árboles o sólo listas, vemos que no hay mucha diferencia en el tiempo de carga para ambos requerimientos. En el req2 del lab 5 la carga de solo árbol toma 0.09s y la carga de solo lista toma 0.07s. Por otro lado, en el req3 del lab6 la carga de solo árbol toma 0.15s y la de solo lista toma lo mismo.

¿En un hashmap es posible hacer una búsqueda por rango de llaves? ¿Que complejidad tendría?

Sí es posible pero si no se hace sobre tablas de hash sería ineficiente. Básicamente se tiene un hashmap dentro de otro.