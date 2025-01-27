class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol():
    valor = input("Ingrese el valor del nodo (operador u operando): ").strip()
    nodo = Nodo(valor if valor in "+-*/" else float(valor))  # Convertir a número si es operando
    
    tiene_izquierdo = input(f"¿El nodo '{valor}' tiene hijo izquierdo? (s/n): ").strip().lower()
    if tiene_izquierdo == 's':
        print(f"Construyendo subárbol izquierdo de '{valor}'...")
        nodo.izquierdo = construir_arbol()

    tiene_derecho = input(f"¿El nodo '{valor}' tiene hijo derecho? (s/n): ").strip().lower()
    if tiene_derecho == 's':
        print(f"Construyendo subárbol derecho de '{valor}'...")
        nodo.derecho = construir_arbol()

    return nodo

def evaluar_arbol(nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor

    izquierdo = evaluar_arbol(nodo.izquierdo)
    derecho = evaluar_arbol(nodo.derecho)

    if nodo.valor == '+':
        return izquierdo + derecho
    elif nodo.valor == '-':
        return izquierdo - derecho
    elif nodo.valor == '*':
        return izquierdo * derecho
    elif nodo.valor == '/':
        return izquierdo / derecho

# Construcción y evaluación del árbol
print("Construcción del árbol binario:")
raiz = construir_arbol()

print("\nEvaluando expresión representada por el árbol...")
resultado = evaluar_arbol(raiz)
print("\nResultado de la expresión:", resultado)
