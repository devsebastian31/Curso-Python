# Pedir la edad de los compañeros que vinieron a clase y ordenar los datos de menor a mayor

def obtener_compañeros(cantidad_compañeros):
    compañeros = [] # Inicializa una lista vacía llamada compañeros para almacenar la información de los compañeros.
    # Utiliza un bucle for para iterar a través de la cantidad especificada de compañeros.

    for i in range(cantidad_compañeros):
        nombres = input("Ingrese su Nombre: ")
        edad = int(input("Ingrese la edad: "))

        # Crea una tupla con el nombre y la edad del compañero y la agrega a la lista de compañeros.
        compañero = (nombres, edad)
        compañeros.append(compañero)

        # El parámetro key en la función sort sirve para especificar una función de clave personalizada que determina el orden de clasificación
    compañeros.sort(key=lambda x: x[1]) # Ordena la lista de compañeros en función de la edad, de menor a mayor.

    asistente = compañeros[0][0]# Obtiene el nombre del asistente, que es el compañero más joven.

    profesor = compañeros[-1][0]# Obtiene el nombre del profesor, que es el compañero de mayor edad.

    return asistente, profesor # Devuelve los nombres del asistente y del profesor como una tupla.

# Llama a la función obtener_compañeros con un argumento de 5 compañeros y almacena los resultados en asistente y profesor.
asistente, profesor = obtener_compañeros(5)
print(f"El profesor es: {profesor} y su asistente es {asistente}") # Imprime el nombre del profesor y su asistente.
