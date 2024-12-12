class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if not actual:
            print("Canción no encontrada.")
            return
        if not anterior:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        print(f"Canción '{dato}' eliminada.")

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def recorrer(self):
        actual = self.cabeza
        if not actual:
            print("La playlist está vacía.")
        while actual:
            print(f" - {actual.dato}")
            actual = actual.siguiente
