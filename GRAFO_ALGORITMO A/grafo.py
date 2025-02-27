import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)

    def agregar_arista(self, nodo1, nodo2, peso):
        self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def mostrar_grafo(self):
        pos = nx.spring_layout(self.grafo)
        labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw(self.grafo, pos, with_labels=True, node_color='lightblue', node_size=1000, edge_color='gray')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

def heuristica(nodo, objetivo):
    return abs(nodo - objetivo)  # Heurística simple basada en la diferencia de índices

def a_estrella(grafo, inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))
    costos = {inicio: 0}
    caminos = {inicio: None}

    print("\n🚀 Ejecutando A* estándar...")
    
    while cola:
        _, nodo_actual = heapq.heappop(cola)
        print(f"🔍 Visitando nodo: {nodo_actual}")

        if nodo_actual == objetivo:
            ruta = []
            while nodo_actual is not None:
                ruta.append(nodo_actual)
                nodo_actual = caminos[nodo_actual]
            ruta.reverse()
            print(f"✅ Ruta encontrada: {ruta}")
            return ruta

        for vecino in grafo.grafo.neighbors(nodo_actual):
            peso = grafo.grafo[nodo_actual][vecino]['weight']
            costo_nuevo = costos[nodo_actual] + peso

            if vecino not in costos or costo_nuevo < costos[vecino]:
                costos[vecino] = costo_nuevo
                prioridad = costo_nuevo + heuristica(vecino, objetivo)
                heapq.heappush(cola, (prioridad, vecino))
                caminos[vecino] = nodo_actual
                print(f"🟢 Agregando a la cola: {vecino} con costo {costo_nuevo}")

    print("❌ No se encontró ruta")
    return None

def a_estrella_optimizado(grafo, inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))
    costos = {inicio: 0}
    caminos = {inicio: None}
    visitados = set()

    print("\n🚀 Ejecutando A* optimizado...")

    while cola:
        _, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        print(f"🔍 Visitando nodo: {nodo_actual}")
        visitados.add(nodo_actual)

        if nodo_actual == objetivo:
            ruta = []
            while nodo_actual is not None:
                ruta.append(nodo_actual)
                nodo_actual = caminos[nodo_actual]
            ruta.reverse()
            print(f"✅ Ruta encontrada: {ruta}")
            return ruta

        for vecino in grafo.grafo.neighbors(nodo_actual):
            peso = grafo.grafo[nodo_actual][vecino]['weight']
            costo_nuevo = costos[nodo_actual] + peso

            if vecino not in costos or costo_nuevo < costos[vecino]:
                costos[vecino] = costo_nuevo
                prioridad = costo_nuevo + heuristica(vecino, objetivo)
                heapq.heappush(cola, (prioridad, vecino))
                caminos[vecino] = nodo_actual
                print(f"🟢 Agregando a la cola: {vecino} con costo {costo_nuevo}")

    print("❌ No se encontró ruta")
    return None

# 🔹 Creación del grafo y prueba del algoritmo
grafo = Grafo()
for nodo in range(1, 8):
    grafo.agregar_nodo(nodo)

grafo.agregar_arista(1, 2, 2)
grafo.agregar_arista(1, 3, 4)
grafo.agregar_arista(2, 3, 1)
grafo.agregar_arista(2, 4, 7)
grafo.agregar_arista(2, 5, 3)
grafo.agregar_arista(3, 6, 5)
grafo.agregar_arista(4, 5, 2)
grafo.agregar_arista(5, 6, 4)
grafo.agregar_arista(5, 7, 1)
grafo.agregar_arista(6, 7, 6)

# 🔹 Mostrar estructura del grafo
print("\n📌 Nodos del grafo:", grafo.grafo.nodes)
print("📌 Aristas del grafo:", list(grafo.grafo.edges(data=True)))

# 🔹 Ejecutar algoritmos
ruta_estandar = a_estrella(grafo, 1, 7)
ruta_optimizada = a_estrella_optimizado(grafo, 1, 7)

# 🔹 Mostrar resultados
print(f"\n🌟 Ruta con A* estándar: {ruta_estandar}")
print(f"🌟 Ruta con A* optimizado: {ruta_optimizada}")

# 🔹 Mostrar grafo
grafo.mostrar_grafo()
