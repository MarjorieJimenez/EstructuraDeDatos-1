import time

# Codigo original
def calcular_suma_original(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

# Prueba con una lista grande
lista_grande = list(range(1000000))  

# Medicion de tiempo para el codigo original
start_time = time.time()
calcular_suma_original(lista_grande)
original_time = time.time() - start_time


# Imprimir los resultados
print(f"Tiempo de ejecución (Codigo original): {original_time} segundos")

