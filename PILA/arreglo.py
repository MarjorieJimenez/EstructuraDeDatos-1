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

# Interacción con el usuario
def main():
    stack = ArrayStack()
    while True:
        print("\nOpciones:")
        print("1. Apilar (push)")
        print("2. Desapilar (pop)")
        print("3. Consultar elemento superior (peek)")
        print("4. Verificar si la pila esta vacía (is_empty)")
        print("5. Salir")
        choice = input("Selecciona una opcion (1-5): ")

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
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
