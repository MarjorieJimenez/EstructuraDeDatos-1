# Implementación de un TDA y creación de una aplicación simple

# Selección del TDA y la Aplicación

TDA elegido: Pila.
Para esta actividad, vamos a elegir una pila para evaluar expresiones matemáticas. Este TDA es ideal para el análisis de expresiones, ya que se puede utilizar para evaluar expresiones aritméticas y otros tipos de cálculos que requieren un orden de operaciones.

#  Investigación y Diseño

Investigación sobre la pila en Python: Una pila es una estructura de datos que sigue el principio de LIFO (Last In, First Out). Esto significa que el último elemento agregado es el primero en ser eliminado. Las operaciones básicas que se implementan son:

push(item): Agrega un elemento a la pila.
pop(): Elimina y devuelve el último elemento de la pila.
peek(): Muestra el último elemento sin eliminarlo.
is_empty(): Verifica si la pila está vacía.
Para implementar un evaluador de expresiones, la pila se puede utilizar para manejar los operadores y operandos mientras se procesan los tokens de la expresión.

Diseño básico:
Interfaz de entrada: El usuario ingresará una expresión matemática.
Procesamiento: Se recorrerá la expresión de izquierda a derecha, evaluando y almacenando valores y operadores en la pila.
Salida: El resultado de la evaluación se imprimirá.

# Explicación del Código:

Pila: Mantiene los valores y operadores mientras se procesa la expresión.
Prioridad de operadores: La función prioridad determina qué operadores tienen mayor precedencia (* y / tienen mayor prioridad que + y -).
Evaluación infija: La función evaluar_expresion convierte una expresión infija en una forma evaluable usando pilas:
Los números se apilan directamente.
Los operadores se apilan, pero si hay un operador con mayor o igual prioridad en la pila de operadores, se resuelven antes.
Los paréntesis son manejados para asegurar que las operaciones dentro de ellos se resuelvan primero.
Ingreso por consola: El usuario puede ingresar la expresión en la forma tradicional, con espacios entre los operadores y números.
