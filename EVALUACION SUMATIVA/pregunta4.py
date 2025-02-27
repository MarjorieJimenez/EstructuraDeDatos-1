class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ColaDobleEnlazada:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.final is None:  # Si la cola está vacía
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.final
            self.final = nuevo_nodo
        self.tamano += 1

    def dequeue(self):
        if self.frente is None:
            raise Exception("La cola está vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None  # La cola está vacía
        else:
            self.frente.anterior = None
        self.tamano -= 1
        return valor

    def peek(self):
        if self.frente is None:
            return None
        return self.frente.valor

    def esta_vacia(self):
        return self.frente is None

    def tamano_cola(self):
        return self.tamano

# Prueba de la implementación
cola = ColaDobleEnlazada()
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Primer elemento:", cola.peek())  # Salida esperada: 10
print("Eliminando:", cola.dequeue())   # Salida esperada: 10
print("Nuevo primer elemento:", cola.peek())  # Salida esperada: 20
