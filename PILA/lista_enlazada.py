class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pila vacia")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Pila vacia")
        return self.top.data

    def is_empty(self):
        return self.top is None

# Programa principal
def main():
    stack = LinkedListStack()
    while True:
        print("\nOpciones:")
        print("1. Apilar (push)")
        print("2. Desapilar (pop)")
        print("3. Consultar el elemento superior (peek)")
        print("4. Verificar si la pila está vacia (isEmpty)")
        print("5. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            elemento = input("Ingresa el elemento a apilar: ")
            stack.push(elemento)
            print(f"'{elemento}' apilado correctamente.")
        elif opcion == "2":
            try:
                desapilado = stack.pop()
                print(f"Elemento desapilado: {desapilado}")
            except IndexError as e:
                print(e)
        elif opcion == "3":
            try:
                elemento_superior = stack.peek()
                print(f"Elemento superior: {elemento_superior}")
            except IndexError as e:
                print(e)
        elif opcion == "4":
            if stack.is_empty():
                print("La pila esta vacia.")
            else:
                print("La pila no está vacia.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
import logging

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        logging.basicConfig(level=logging.INFO)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        logging.info(f"Element '{data}' pushed to the stack.")

    def pop(self):
        if self.is_empty():
            logging.error("Stack is empty")
            raise IndexError("Pila vacia")
        data = self.top.data
        self.top = self.top.next
        logging.info(f"Element '{data}' popped from the stack.")
        return data

    def peek(self):
        if self.is_empty():
            logging.error("Stack is empty")
            raise IndexError("Pila vacía")
        logging.info(f"Peeked element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        logging.info("Checked if stack is empty")
        return self.top is None

# Programa principal
def main():
    stack = LinkedListStack()
    while True:
        print("\nOpciones:")
        print("1. Apilar (push)")
        print("2. Desapilar (pop)")
        print("3. Consultar el elemento superior (peek)")
        print("4. Verificar si la pila está vacía (isEmpty)")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            elemento = input("Ingresa el elemento a apilar: ")
            stack.push(elemento)
            print(f"'{elemento}' apilado correctamente.")
        elif opcion == "2":
            try:
                desapilado = stack.pop()
                print(f"Elemento desapilado: {desapilado}")
            except IndexError as e:
                print(e)
        elif opcion == "3":
            try:
                elemento_superior = stack.peek()
                print(f"Elemento superior: {elemento_superior}")
            except IndexError as e:
                print(e)
        elif opcion == "4":
            if stack.is_empty():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()