class Paciente:
    """Clase que representa a un paciente con prioridad."""
    def __init__(self, id, nombre, prioridad):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad  # Menor número = mayor urgencia

    def __str__(self):
        return f"[ID: {self.id}] {self.nombre} - Prioridad: {self.prioridad}"


class NodoAVL:
    """Nodo del árbol AVL que almacena un paciente."""
    def __init__(self, paciente):
        self.paciente = paciente
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    """Implementación del árbol AVL para manejar la gestión de turnos."""
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        """Devuelve la altura de un nodo."""
        return nodo.altura if nodo else 0

    def get_balance(self, nodo):
        """Calcula el factor de balance de un nodo."""
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0

    def rotacion_derecha(self, y):
        """Rotación derecha en el nodo y."""
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        return x

    def rotacion_izquierda(self, x):
        """Rotación izquierda en el nodo x."""
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        return y

    def insertar(self, nodo, paciente):
        """Inserta un paciente en el árbol AVL."""
        if not nodo:
            return NodoAVL(paciente)

        if paciente.prioridad < nodo.paciente.prioridad:
            nodo.izq = self.insertar(nodo.izq, paciente)
        else:
            nodo.der = self.insertar(nodo.der, paciente)

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        balance = self.get_balance(nodo)

        # Rotaciones para balancear
        if balance > 1 and paciente.prioridad < nodo.izq.paciente.prioridad:
            return self.rotacion_derecha(nodo)
        if balance < -1 and paciente.prioridad > nodo.der.paciente.prioridad:
            return self.rotacion_izquierda(nodo)
        if balance > 1 and paciente.prioridad > nodo.izq.paciente.prioridad:
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)
        if balance < -1 and paciente.prioridad < nodo.der.paciente.prioridad:
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo

    def agregar_paciente(self, paciente):
        """Método público para insertar un paciente."""
        self.raiz = self.insertar(self.raiz, paciente)

    def obtener_paciente_prioritario(self, nodo):
        """Encuentra el paciente con mayor prioridad (menor número)."""
        if nodo is None or nodo.izq is None:
            return nodo
        return self.obtener_paciente_prioritario(nodo.izq)

    def eliminar_paciente_prioritario(self, nodo):
        """Elimina el paciente con mayor prioridad y retorna el nuevo nodo raíz."""
        if nodo.izq is None:
            return nodo.der
        nodo.izq = self.eliminar_paciente_prioritario(nodo.izq)
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
        
        balance = self.get_balance(nodo)

        # Balanceo del árbol AVL
        if balance > 1 and self.get_balance(nodo.izq) >= 0:
            return self.rotacion_derecha(nodo)
        if balance > 1 and self.get_balance(nodo.izq) < 0:
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)
        if balance < -1 and self.get_balance(nodo.der) <= 0:
            return self.rotacion_izquierda(nodo)
        if balance < -1 and self.get_balance(nodo.der) > 0:
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo

    def atender_paciente(self):
        """Atiende al paciente con mayor prioridad."""
        if self.raiz is None:
            print("No hay pacientes en espera.")
            return
        
        paciente_prioritario = self.obtener_paciente_prioritario(self.raiz)
        print(f"🩺 Atendiendo a: {paciente_prioritario.paciente}")
        
        self.raiz = self.eliminar_paciente_prioritario(self.raiz)

    def mostrar_pacientes(self):
        """Muestra los pacientes en orden de prioridad."""
        if self.raiz is None:
            print("No hay pacientes registrados.")
        else:
            print("\n📋 Lista de pacientes ordenados por prioridad:")
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        """Recorre el árbol en inorden para mostrar los pacientes correctamente."""
        if nodo:
            self._inorden(nodo.izq)
            print(nodo.paciente)
            self._inorden(nodo.der)


# --- MENÚ INTERACTIVO ---
avl = ArbolAVL()
contador_id = 1  # ID autoincremental

while True:
    print("\n🚑 GESTIÓN DE TURNOS EN HOSPITAL")
    print("1. Agregar paciente")
    print("2. Mostrar pacientes")
    print("3. Atender paciente")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        prioridad = int(input("Ingrese la prioridad (1 = emergencia, 10 = menos urgente): "))
        nuevo_paciente = Paciente(contador_id, nombre, prioridad)
        avl.agregar_paciente(nuevo_paciente)
        print(f"✅ Paciente {nombre} agregado con prioridad {prioridad}.")
        contador_id += 1

    elif opcion == "2":
        avl.mostrar_pacientes()

    elif opcion == "3":
        avl.atender_paciente()

    elif opcion == "4":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("⚠️ Opción no válida, intente nuevamente.")
