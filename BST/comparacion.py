import time

# Definición del Nodo del BST
class Nodo:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.izquierda = None
        self.derecha = None

# Implementación del BST
class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, telefono):
        if self.raiz is None:
            self.raiz = Nodo(nombre, telefono)
        else:
            self._insertar_recursivo(self.raiz, nombre, telefono)

    def _insertar_recursivo(self, nodo, nombre, telefono):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre, telefono)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre, telefono)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre, telefono)
            else:
                self._insertar_recursivo(nodo.derecha, nombre, telefono)

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        return self._buscar_recursivo(nodo.derecha, nombre)

# Implementación de la Lista
class ListaContactos:
    def __init__(self):
        self.contactos = []

    def insertar(self, nombre, telefono):
        self.contactos.append((nombre, telefono))

    def buscar(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                return contacto
        return None

# Función para medir tiempos de búsqueda
def medir_tiempo_busqueda(estructura, nombre):
    inicio = time.perf_counter()
    resultado = estructura.buscar(nombre)
    fin = time.perf_counter()
    return resultado, fin - inicio

# Ingreso de datos por consola
def ingresar_contactos(estructura_lista, estructura_bst, cantidad):
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        estructura_lista.insertar(nombre, telefono)
        estructura_bst.insertar(nombre, telefono)

# Ejecución del programa
if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad de contactos a agregar: "))

    # Inicializar estructuras
    lista_contactos = ListaContactos()
    bst_contactos = BST()

    # Ingresar datos manualmente
    ingresar_contactos(lista_contactos, bst_contactos, cantidad)

    # Buscar un contacto
    busqueda_nombre = input("Ingrese el nombre a buscar: ")

    # Comparación de tiempos
    resultado_lista, tiempo_lista = medir_tiempo_busqueda(lista_contactos, busqueda_nombre)
    resultado_bst, tiempo_bst = medir_tiempo_busqueda(bst_contactos, busqueda_nombre)

    print(f"\n🔍 Resultados de búsqueda:")
    print(f"  - En Lista: {'Encontrado' if resultado_lista else 'No encontrado'} en {tiempo_lista:.9f} segundos")
    print(f"  - En BST: {'Encontrado' if resultado_bst else 'No encontrado'} en {tiempo_bst:.9f} segundos")

