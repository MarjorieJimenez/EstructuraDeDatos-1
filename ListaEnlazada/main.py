from lista_enlazada import ListaEnlazada

def menu():
    print("\n--- Gestion de Playlist de Musica ---")
    print("1. Agregar cancion")
    print("2. Eliminar cancion")
    print("3. Buscar cancion")
    print("4. Mostrar playlist")
    print("5. Salir")
    return int(input("Seleccione una opcion: "))

if __name__ == "__main__":
    playlist = ListaEnlazada()
    while True:
        opcion = menu()
        if opcion == 1:
            cancion = input("Ingrese el nombre de la cancion: ")
            playlist.insertar(cancion)
            print(f"Cancion '{cancion}' agregada")
        elif opcion == 2:
            cancion = input("Ingrese el nombre de la cancion a eliminar: ")
            playlist.eliminar(cancion)
        elif opcion == 3:
            cancion = input("Ingrese el nombre de la cancion a buscar: ")
            posicion = playlist.buscar(cancion)
            if posicion != -1:
                print(f"La cancion '{cancion}' se encuentra en la posicion {posicion}")
            else:
                print("Cancion no encontrada")
        elif opcion == 4:
            print("Playlist actual:")
            playlist.recorrer()
        elif opcion == 5:
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida. Intente nuevamente")
