class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pila vacia")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Pila vacia")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Evaluar expresiones en notación posfija
def evaluate_postfix(expression):
    stack = ArrayStack()
    for token in expression.split():
        if token.isdigit():  # Operando
            stack.push(int(token))
        else:  # Operador
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    return stack.pop()

# Interacción con el usuario
def main():
    stack = ArrayStack()
    while True:
        print("\nOpciones:")
        print("1. Apilar (push)")
        print("2. Desapilar (pop)")
        print("3. Consultar elemento superior (peek)")
        print("4. Verificar si la pila esta vacía (is_empty)")
        print("5. Evaluar expresión en notación posfija")
        print("6. Salir")
        choice = input("Selecciona una opcion (1-6): ")

        if choice == "1":
            data = input("Introduce el dato a apilar: ")
            stack.push(data)
            print(f"Elemento '{data}' apilado.")
        elif choice == "2":
            try:
                popped = stack.pop()
                print(f"Elemento desapilado: {popped}")
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                top = stack.peek()
                print(f"Elemento superior: {top}")
            except IndexError as e:
                print(e)
        elif choice == "4":
            if stack.is_empty():
                print("La pila está vacia.")
            else:
                print("La pila no esta vacía.")
        elif choice == "5":
            expression = input("Introduce la expresión en notación posfija (separada por espacios): ")
            try:
                result = evaluate_postfix(expression)
                print(f"Resultado de la expresión: {result}")
            except IndexError:
                print("Error: Expresión no válida.")
            except ZeroDivisionError:
                print("Error: División por cero.")
        elif choice == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
