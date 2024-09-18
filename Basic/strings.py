myStr = "hello Word"

# print(dir(myStr)) dir nos enseña que podemos hacer con cierto tipo de dato

print(myStr.upper()) # mayuscula

print(myStr.lower()) # minuscula

print(myStr.swapcase()) # convierte mayusculas a minusculas y al reves XD

print(myStr.capitalize()) # convierte en mayuscula la primer letra

print(len(myStr)) # Calcular la longitud del contenido de la variable 

print(myStr.replace('hello' , 'bye').upper()) # sirve para remplazar por otra palabra

print(myStr.count('d')) # sirve para contar cuantas veces se ha repetido una letra

print(myStr.startswith('hello')) # Sirve para verificar si el texto que esta escrito empiesa con hola o con hello

print(myStr.endswith('Word')) # Sirve para verificar si la palabra final termina en Word

print(myStr.split('o')) # split separa el texto basado en un espacio, tambien puede separar bazado en una de la o

print(myStr.find('d')) # find sirve para buscar una letra

print(len(myStr)) # sirve para saver la longitud del string

print(myStr.index('e')) # Aqui sirve para saber el indice de una letra

print(myStr.isnumeric()) # sirve para saber si mystr es numerico
print(myStr.isalpha()) # sirve para saber si es alfanumerico
print(myStr.isdigit()) # sirve para saber si contiene únicamente caracteres numéricos.

print(myStr[0]) # sirve para saber que letra esta en la posicion 0
print(myStr[-3]) # sirve para saber que letra esta en la posicion -3

# Formateo

name, surname, age = "Sebastian", "Alejandro", 18
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Aqui para hacer con .format se debe hacer con {}
print("Mi nombre es %s %s y mi edad es %s" % (name, surname, age)) # Aqui %s le estamos diciendo que le primero valor lo incerte en %s
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # La f sirve para formatear e ir infiriendo en cada variable

# Desempaqueado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a) # p
print(e) # e

# División

language_slice = language[1:3] # Aqui no muestra de la 1 a la 3 si contar la 3 osea yt
print(language_slice)

language_slice = language[1:] # Aqui solo nos muestra desde la 1 osea ython
print(language_slice)

language_slice = language[-2] # Aqui comienza desde el final y la segunda letra es la o
print(language_slice)

language_slice = language[0:6:2] # Aqui estamos diciendo que del 0 al 6 nos muestre todos y luego nos muestre del 0 al 2 osea Pto
print(language_slice)

# Reverse

reversed_language = language[::-1] # Aqui invierte la palabra y muestra nohtyp
print(reversed_language)