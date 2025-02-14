class Nodo:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, telefono):
        self.raiz = self._insertar_recursivo(self.raiz, nombre, telefono)

    def _insertar_recursivo(self, nodo, nombre, telefono):
        if nodo is None:
            return Nodo(nombre, telefono)
        if nombre < nodo.nombre:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, nombre, telefono)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, nombre, telefono)
        return nodo

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        return self._buscar_recursivo(nodo.derecha, nombre)

    def mostrar_en_orden(self):
        self._in_order(self.raiz)

    def _in_order(self, nodo):
        if nodo is not None:
            self._in_order(nodo.izquierda)
            print(f"Nombre: {nodo.nombre}, Teléfono: {nodo.telefono}")
            self._in_order(nodo.derecha)

# --- Programa con Interacción en Consola ---
agenda = BST()

while True:
    print("\nMenu de la Agenda:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos ordenados")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono: ")
        agenda.insertar(nombre, telefono)
        print(f"Contacto '{nombre}' agregado con exito.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        contacto = agenda.buscar(nombre)
        if contacto:
            print(f"Contacto encontrado: {contacto.nombre}, Telefono: {contacto.telefono}")
        else:
            print(f"{nombre} no se encuentra en la agenda.")

    elif opcion == "3":
        print("\nContactos ordenados:")
        agenda.mostrar_en_orden()

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opcion no valida, intente nuevamente.")
