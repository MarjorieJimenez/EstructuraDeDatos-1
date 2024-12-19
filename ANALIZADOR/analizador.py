class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class AnalizadorSintactico:
    def __init__(self):
        self.operadores = {'+', '-', '*', '/'}
        self.parentesis_abiertos = {'(', '[', '{'}
        self.parentesis_cerrados = {')', ']', '}'}
        self.pares_parentesis = {'(': ')', '[': ']', '{': '}'}

    def validar_balanceo(self, expresion):
        stack = []
        for i, char in enumerate(expresion):
            if char in self.parentesis_abiertos:
                stack.append(char)
            elif char in self.parentesis_cerrados:
                if not stack or self.pares_parentesis[stack.pop()] != char:
                    return f"Error: Paréntesis desbalanceados en la posición {i}"
        return "Expresión válida" if not stack else "Error: Paréntesis desbalanceados"

    def validar_disposicion(self, expresion):
        tokens = self.tokenizar(expresion)
        prev = None
        for i, token in enumerate(tokens):
            if token in self.operadores:
                if prev is None or prev in self.operadores or prev in self.parentesis_abiertos:
                    return f"Error: Operador inesperado en la posición {i}"
            elif token in self.parentesis_cerrados:
                if prev in self.operadores or prev in self.parentesis_abiertos:
                    return f"Error: Paréntesis de cierre inesperado en la posición {i}"
            prev = token
        return "Disposición válida"

    def tokenizar(self, expresion):
        tokens = []
        temp = ''
        for char in expresion:
            if char.isspace():
                continue
            if char in self.operadores or char in self.parentesis_abiertos | self.parentesis_cerrados:
                if temp:
                    tokens.append(temp)
                    temp = ''
                tokens.append(char)
            else:
                temp += char
        if temp:
            tokens.append(temp)
        return tokens

    def convertir_a_posfija(self, expresion):
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida = []
        stack = []
        tokens = self.tokenizar(expresion)
        for token in tokens:
            if token.isalnum():
                salida.append(token)
            elif token in self.operadores:
                while stack and stack[-1] != '(' and precedencia.get(stack[-1], 0) >= precedencia[token]:
                    salida.append(stack.pop())
                stack.append(token)
            elif token in self.parentesis_abiertos:
                stack.append(token)
            elif token in self.parentesis_cerrados:
                while stack and stack[-1] not in self.parentesis_abiertos:
                    salida.append(stack.pop())
                stack.pop()  # Eliminar el paréntesis de apertura correspondiente
        while stack:
            salida.append(stack.pop())
        return salida

    def construir_arbol(self, posfija):
        stack = []
        for token in posfija:
            nodo = NodoArbol(token)
            if token in self.operadores:
                nodo.derecho = stack.pop()
                nodo.izquierdo = stack.pop()
            stack.append(nodo)
        return stack.pop()

    def imprimir_arbol(self, nodo, nivel=0):
        if nodo:
            self.imprimir_arbol(nodo.derecho, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.valor)
            self.imprimir_arbol(nodo.izquierdo, nivel + 1)

    def analizar(self, expresion):
        balanceo = self.validar_balanceo(expresion)
        if "Error" in balanceo:
            return balanceo
        disposicion = self.validar_disposicion(expresion)
        if "Error" in disposicion:
            return disposicion
        posfija = self.convertir_a_posfija(expresion)
        arbol = self.construir_arbol(posfija)
        print("Árbol de expresión:")
        self.imprimir_arbol(arbol)
        return "Expresión válida y árbol generado."

# Ejemplo de uso con entrada por consola
if __name__ == "__main__":
    analizador = AnalizadorSintactico()
    while True:
        expresion = input("\nIngresa una expresión matemática (o escribe 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            print("Finalizando el programa. ¡Adiós!")
            break
        resultado = analizador.analizar(expresion)
        print(resultado)
