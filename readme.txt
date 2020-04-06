Nicolas Caicedo Murgueitio 201820789
Vytis Karanauskas 201912961

REFLEXIÓN


1. ¿Cómo se utilizaron las estructuras de datos vistas en clase?
En el reto tres se usaron muchas estructuras de datos, estas incluyen pero no se limitan a: red-black tree para organizar la información de los accidentes en el catálogo, utilizamos tablas dentro de algunos nodos, utilizamos ordenamientos para hacer que los datos estén de mayor a menor cuando se nos pedía. Principalmente usamos bst no solo para organizar la información si no también para recorrerla.


2. ¿Cuáles campos seleccionaron para definir la llave de los árboles, y cómo generaliza esta solución a otros tipos de problemas similares?
En nuestro caso, nos fuimos con id, severity, start time y state. Estos se usaron en diferentes ocaciones según su necesidad. Nuestra solución es aplicable a datos similares, hay que cambiar un par de variables de carga pero en general es una solución versátil.


3. ¿Qué ventajas ofrece el uso de árboles sobre las estructuras de datos vistas anteriormente?
Principalmente su velocidad, el caso promedio de búsqueda de un dato en un bst de la raíz a la hoja puede tomar log_2 N (y en el peor caso 3logN), esto es realmente rápido comparado con otras estructuras. De igual manera la cantidad de información se va disminuyendo a medida que se baja por los nodos. Los nodos son a su vez realmente útiles por su versatilidad, en ellos podemos entrar desde tablas de hash hasta listas.


4. ¿En qué escenarios recomendaría utilizar árboles BST o árboles Red-Black?
Primero hay que entender que en un bst importa cómo llegan los datos, ya que si no llegan en un orden adecuado el árbol puede quedar desbalanceado, por otro lado, los rbt sirven cuando la información llega sin orden, aunque toma más tiempo se logra tener un árbol balanceado independiente de los datos.
Entonces: si tengo datos ordenados de manera correcta, uso bst, si no los tengo uso rbt.


5. ¿A qué conclusiones llegan a partir de analizar los resultados de complejidad temporal entre árboles binarios ordenados (BST) y Red-black?
Juzgando por el tiempo nos podemos dar cuenta a simple vista que la complejidad de un rbt es mayor. Este reto tarda en cargar los datos aproximadamente 1.3s mientras que implementando con un bst tarda 0.15s según los laboratorios anteriores.