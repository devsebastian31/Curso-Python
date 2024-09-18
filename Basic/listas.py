number_list = list((1,2,3,4)) # list solo soporta 1 argumento para que soporte 4 debo crear una tupla
print((number_list))

r = list(range(1, 11)) # Aqui mostrara del 1 al 10
print(r)

lista = ["Hello","Bye","Adios"]
# print(dir(lista)) # dir sirve para saber que datos puedes ejecutar de una lista

print(lista[1]) # Imprime la letra de la posicion 1
lista.append("God") # append sirve para agregar un nuevo elemento
lista.extend(["Blue","Red"]) # extend Sirve para extender basado en esta lista
lista.insert(1, "Black") # insert Sirve para insertar en cierta posicion un nuevo elemento
lista.insert(len(lista), "Orange") # Aqui len sirve para la longitud y agregar al ultimo un nuevo elemento
print(lista.index("Red")) # index sirve para saber el indice
print(lista.count("Red")) # Sirve para contar cuantas veces existe ese elemento
print(lista)
lista.sort() # sort sirve para ordenar alfabeticamente
lista.sort(reverse=True) # Sirve para ordenar alfabeticamente invera
lista.pop() # pop sirve para quitar un elemento, tambien se puede quitar segun el indice
lista.remove("God") # remove sirve para remover un elemento
lista.clear() # clear quita todos los elementos
print(lista)