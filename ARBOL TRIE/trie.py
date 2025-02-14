class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin_de_palabra = False


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra):
        nodo = self.raiz
        for char in palabra:
            if char not in nodo.hijos:
                nodo.hijos[char] = NodoTrie()
            nodo = nodo.hijos[char]
        nodo.fin_de_palabra = True

    def buscar(self, palabra):
        nodo = self.raiz
        for char in palabra:
            if char not in nodo.hijos:
                return False
            nodo = nodo.hijos[char]
        return nodo.fin_de_palabra

    def buscar_prefijo(self, prefijo):
        nodo = self.raiz
        for char in prefijo:
            if char not in nodo.hijos:
                return False
            nodo = nodo.hijos[char]
        return True


# Función principal para interactuar con el Trie desde la consola
def menu_trie():
    trie = Trie()

    while True:
        print("\n--- Menú Trie ---")
        print("1. Insertar palabra")
        print("2. Buscar palabra completa")
        print("3. Buscar prefijo")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            palabra = input("Ingresa la palabra a insertar: ").strip().lower()
            trie.insertar(palabra)
            print(f"Palabra '{palabra}' insertada correctamente.")

        elif opcion == "2":
            palabra = input("Ingresa la palabra a buscar: ").strip().lower()
            if trie.buscar(palabra):
                print(f"La palabra '{palabra}' está en el Trie.")
            else:
                print(f"La palabra '{palabra}' NO está en el Trie.")

        elif opcion == "3":
            prefijo = input("Ingresa el prefijo a buscar: ").strip().lower()
            if trie.buscar_prefijo(prefijo):
                print(f"Existen palabras que comienzan con el prefijo '{prefijo}'.")
            else:
                print(f"No existen palabras que comiencen con el prefijo '{prefijo}'.")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamamos al menú principal
if __name__ == "__main__":
    menu_trie()
