# Calcula la suma de los números pares hasta un número dado

# Definición de la función suma_numeros_pares que toma un parámetro n
def suma_numeros_pares(n):
    # Inicialización de la variable suma que almacenará la suma de números pares
    suma = 0
    
    # Bucle for que itera sobre los números pares desde 2 hasta n (incluyendo n) de 2 en 2
    for i in range(2, n+1, 2):
        # Se suma el número actual al valor acumulado en la variable suma
        suma += i # 0+2 luego 2+4 luego 6+6 luego 12+8
    
    # Se devuelve el resultado de la suma de números pares
    return suma

# Ejemplo de uso de la función con n=8
resultado = suma_numeros_pares(8) # En este caso se suma 2+4+6+8 hasta el 8

# Se imprime el resultado de la suma de números pares
print("La suma de números pares es:", resultado)

