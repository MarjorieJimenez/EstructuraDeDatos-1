import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# Datos simulados (sin IA)
prioridades = np.array([1, 2, 3, 4, 5])  # Niveles de prioridad
tiempos_sin_ia = np.array([10, 15, 20, 25, 30])  # Tiempos de espera iniciales

# Datos para entrenar el modelo (introducimos una dependencia más marcada)
# Prioridad y "carga del sistema" como factores
X_entrenamiento = np.array([
    [1, 0.8],
    [2, 0.6],
    [3, 0.5],
    [4, 0.3],
    [5, 0.1]
])

# Tiempos de espera objetivo (con un comportamiento no lineal)
y_entrenamiento = np.array([9, 12, 16, 21, 26])

# Crear el modelo de IA
modelo = Sequential([
    Dense(10, input_dim=2, activation='relu'),
    Dense(5, activation='relu'),
    Dense(1, activation='linear')
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# Entrenar el modelo
modelo.fit(X_entrenamiento, y_entrenamiento, epochs=500, verbose=0)

# Generar predicciones para las mismas prioridades
X_prueba = np.array([
    [1, 0.8],
    [2, 0.6],
    [3, 0.5],
    [4, 0.3],
    [5, 0.1]
])
tiempos_con_ia = modelo.predict(X_prueba).flatten()

# Comparar resultados
print("Simulación sin IA:", tiempos_sin_ia)
print("Simulación con IA (predicciones):", tiempos_con_ia)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(prioridades, tiempos_sin_ia, label="Sin IA", marker="o", color="blue")
plt.plot(prioridades, tiempos_con_ia, label="Con IA", marker="o", linestyle="--", color="green")

# Configuración del gráfico
plt.title("Comparación: Simulación con IA vs Sin IA")
plt.xlabel("Prioridad")
plt.ylabel("Tiempo de espera (segundos)")
plt.legend()
plt.grid()
plt.show()
