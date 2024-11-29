import time

# Codigo optimizado
def calcular_suma_optimizada(lista):
    suma = 0
    for item in lista:
        suma += item
    return suma

# Prueba con una lista grande
lista_grande = list(range(1000000))  

# Medicion de tiempo para el codigo optimizado
start_time = time.time()
calcular_suma_optimizada(lista_grande)
optimized_time = time.time() - start_time

# Imprimir los resultados
print(f"Tiempo de ejecución (Codigo optimizado): {optimized_time} segundos")