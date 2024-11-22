# Implementación de la Pila
class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# Prioridad de los operadores
def prioridad(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# Función para evaluar una expresión infija
def evaluar_expresion(exp):
    pila_valores = Pila()
    pila_operadores = Pila()
    
    # Convertir la expresión en una lista de tokens
    tokens = exp.split()
    
    for token in tokens:
        if token.isdigit():  # Si el token es un número
            pila_valores.push(int(token))
        elif token == '(':  # Si es un paréntesis de apertura
            pila_operadores.push(token)
        elif token == ')':  # Si es un paréntesis de cierre
            while pila_operadores.peek() != '(':
                op = pila_operadores.pop()
                val2 = pila_valores.pop()
                val1 = pila_valores.pop()
                if op == '+':
                    pila_valores.push(val1 + val2)
                elif op == '-':
                    pila_valores.push(val1 - val2)
                elif op == '*':
                    pila_valores.push(val1 * val2)
                elif op == '/':
                    pila_valores.push(val1 / val2)
            pila_operadores.pop()  # Eliminar '('
        else:  # Si es un operador (+, -, *, /)
            while (not pila_operadores.is_empty() and
                   prioridad(pila_operadores.peek()) >= prioridad(token)):
                op = pila_operadores.pop()
                val2 = pila_valores.pop()
                val1 = pila_valores.pop()
                if op == '+':
                    pila_valores.push(val1 + val2)
                elif op == '-':
                    pila_valores.push(val1 - val2)
                elif op == '*':
                    pila_valores.push(val1 * val2)
                elif op == '/':
                    pila_valores.push(val1 / val2)
            pila_operadores.push(token)
    
    # Procesar el resto de los operadores
    while not pila_operadores.is_empty():
        op = pila_operadores.pop()
        val2 = pila_valores.pop()
        val1 = pila_valores.pop()
        if op == '+':
            pila_valores.push(val1 + val2)
        elif op == '-':
            pila_valores.push(val1 - val2)
        elif op == '*':
            pila_valores.push(val1 * val2)
        elif op == '/':
            pila_valores.push(val1 / val2)
    
    # El resultado está en la pila de valores
    return pila_valores.pop()

# Ingreso de la expresión por consola
expresion = input("Ingresa la expresión matemática en notación infija (ejemplo: '3 + 4 * 2'): ")
resultado = evaluar_expresion(expresion)
print(f"Resultado: {resultado}")
