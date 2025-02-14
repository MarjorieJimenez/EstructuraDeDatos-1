class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def construir_desde_postfija(self, expresion):
        pila = []
        operadores = {'+', '-', '*', '/'}

        for token in expresion.split():
            if token not in operadores:
                nodo = Nodo(token)
            else:
                nodo = Nodo(token)
                nodo.derecha = pila.pop()
                nodo.izquierda = pila.pop()
            
            pila.append(nodo)

        self.raiz = pila.pop()

    def evaluar(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return float(nodo.valor)

        izquierda_valor = self.evaluar(nodo.izquierda)
        derecha_valor = self.evaluar(nodo.derecha)

        if nodo.valor == '+':
            return izquierda_valor + derecha_valor
        elif nodo.valor == '-':
            return izquierda_valor - derecha_valor
        elif nodo.valor == '*':
            return izquierda_valor * derecha_valor
        elif nodo.valor == '/':
            return izquierda_valor / derecha_valor

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")

# ---- Entrada desde consola ----
expresion_postfija = input("Ingrese una expresion en notacion postfija (ej. '3 5 + 10 2 - *'): ")

# Creando y evaluando el arbol de expresion
arbol = ArbolExpresion()
arbol.construir_desde_postfija(expresion_postfija)

print("\nRecorridos del Arbol:")
print("Preorden: ", end="")
arbol.preorden(arbol.raiz)
print("\nInorden: ", end="")
arbol.inorden(arbol.raiz)
print("\nPostorden: ", end="")
arbol.postorden(arbol.raiz)

resultado = arbol.evaluar(arbol.raiz)
print("\n\nResultado de la expresion:", resultado)
