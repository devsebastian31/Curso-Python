### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

diccionario = { # Un diccionario es una colección de elementos, donde cada uno tiene una llave key y un valor value
  "lat": 1212121212,
  "long": 1212121212,
}

print(diccionario.items()) # items muestra su valor
print(diccionario["lat"] + 5)

print(type({ # type sirve para ver el tipo de dato
"Name":"Sebastian",
  "Lastname":"Zhunaula",
     "Nickname":"NEO",
}))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) # items muestra su valor
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

# fromkeys sirve para crear un nuevo diccionario con claves especificadas y un valor predeterminado opcional en este caso con my_list
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Al crear el diccionario se llenar con none {'Nombre': None, 1: None, 'Piso': None}
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev") # Aqui le decimos que llene el diccionario con MoureDev
print((my_new_dict)) # {'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev', 'Lenguajes': 'MoureDev', 1: 'MoureDev'}

# values nos devuelve todos los valores que contienen un diccionario
my_values = my_new_dict.values() # Obtén los valores del diccionario y guárdalos en la variable my_values
print(type(my_values)) # Imprime el tipo de datos de my_values (por ejemplo, dict_values)

print(my_new_dict.values()) # Imprime directamente los valores del diccionario
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # Convierte los valores del diccionario en una lista, elimina duplicados y convierte de nuevo a lista
# dict se utiliza para almacenar datos en forma de pares clave-valor
print(tuple(my_new_dict)) # Convierte las claves del diccionario en una tupla
print(set(my_new_dict)) # Convierte las claves del diccionario en un conjunto (elimina duplicados)