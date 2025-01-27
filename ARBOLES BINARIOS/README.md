# Implementacion de Arboles Binarios para Evaluacion de Expresiones Lambda

## Descripcion
Este proyecto implementa un arbol binario en Python como herramienta para evaluar expresiones Lambda. Los arboles binarios permiten representar expresiones matematicas o logicas, y mediante un recorrido adecuado (postorden), podemos evaluar dichas expresiones de manera eficiente.

El programa incluye:
- Construccion dinamica del arbol binario.
- Evaluacion recursiva de las expresiones Lambda.
- Pruebas con expresiones predefinidas ingresadas por el usuario.

## Caracteristicas
- **Entrada Dinamica:** Los nodos del arbol se generan con operadores y operandos ingresados por consola.
- **Evaluacion Automatica:** El arbol se recorre en postorden para evaluar la expresion.
- **Compatibilidad con Expresiones Lambda:** Soporte para operaciones basicas como suma, resta, multiplicacion y division.

## Requisitos
- Python 3.7 o superior.
- Entorno de desarrollo como Visual Studio Code, PyCharm o cualquier editor de texto.

## Uso
1. Ejecuta el programa y sigue las instrucciones en pantalla para ingresar una expresion Lambda.
2. Los operadores disponibles son +, -, *, /.
3. Ingresa los operandos en el orden correcto según la estructura de tu expresión.

Ejemplo: Para evaluar (3 + (2 * 4)), ingresa los nodos como:

- Operador raíz: +
- Operando izquierdo: 3
- Operador derecho: *
- Operando izquierdo del nodo *: 2
- Operando derecho del nodo *: 4
- El programa mostrará el resultado 11.
