# Al buscar elementos se comienza desde el 1 
# Al buscas el index se comienza desde el 0

#Lista de datos que si puede modificar
lista1 = [10,20,30,40,55]
lista2 = ["Hello","Bye","Adios"]

print(lista2[2]) # Saber el index de una palabra

#Tupla lista de datos que no puede cambiar XD
tupla = (10,20,30,40,55)

# En un conjunto no puede haber datos duplicados
conjunto = {"Hello","Bye","Adios"}

#Diccionarios sirve para agrupar distintos tipos de datos con un nombre clave
print(type({ # type sirve para ver el tipo de dato
"Name":"Sebastian",
  "Lastname":"Zhunaula",
     "Nickname":"NEO",
}))

diccionario = { # Un diccionario es una colección de elementos, donde cada uno tiene una llave key y un valor value
  "lat": 1212121212,
  "long": 1212121212,
}

print(diccionario.items()) # items muestra su valor
print(diccionario["lat"] + 5)

None #dato que no esta definido