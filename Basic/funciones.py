# def es una definicion de funcion
def hello(name): # name es un parametro
    print("Hello " + name)


hello("Sebas") # Aqui llamamos a al funcion

def add(number1, number2):
    return number1 + number2 # devuelve la suma de ambos


print(add(10, 20))



# Función con parámetros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)



# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")



# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")



# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts): # El * indica que puede recibir múltiples argumentos y los empaqueta en una tupla llamada texts
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")



# Funciones Lambda

# Sirve para crear una funcion anonima o sin nombre

multiplicar = lambda x : x*2

print(multiplicar(4))