def optimized_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Suponemos que el mínimo está en la posición i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  
                min_idx = j  # Encontramos el índice del elemento más pequeño
        
        if min_idx != i:  
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Hacemos el swap solo una vez

    return arr

# Prueba con una lista
arr = [64, 25, 12, 22, 11]
print("Lista ordenada:", optimized_sort(arr))  # Salida esperada: [11, 12, 22, 25, 64]
