# Calcula el factorial de un número

# Definición de la función factorial que toma un parámetro n
def factorial(n):
    # Verifica si n es 0 o 1, en cuyo caso devuelve 1 (caso base)
    if n == 0 or n == 1:
        return 1
    else:
        # Si n no es 0 o 1, calcula el factorial recursivamente
        return n * factorial(n-1)

# Ejemplo de uso de la función con n=5
resultado = factorial(5)
# Imprime el resultado del factorial
print("El factorial de 5 es:", resultado)
