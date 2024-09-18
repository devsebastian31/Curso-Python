### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Sebastian", "Alejandro", 18}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("Sebas")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Sebas")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Sebastian" in my_other_set)
print("Sebastian" in my_other_set)

# Eliminación

my_other_set.remove("Alejandro") # remove sirve para eliminar un elemento de una lista
print(my_other_set)

my_other_set.clear() # clear sirve para eliminar todos los elementos de un diccionario
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Sebastian", "Alejandro", 18}
my_list = list(my_set) # Aqui creamos una tupla apra que list pueda soportar 3 argumentos
print(my_list)
print(my_list[0]) # Aqui imprimimos my_list pero con el argumeto 0

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set) # union sirve para La unión de dos conjuntos
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # Aqui unimos otro congunto
print(my_new_set.difference(my_set)) # difference se utiliza para obtener la diferencia entre dos conjuntos