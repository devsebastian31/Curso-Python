### Operadores Aritméticos ###

# suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5

# Multiplicacion y división (* y /)
multi = 12 * 5
division = 12 / 5

#potenciación (exponente) (**)
exponente = 12**5

# Division baja (//)
division_baja = 12 // 5 # Devuelve entero redondeado hacia abajo

# Resto o módulo
resto = 12 % 5 # Te muestra lo que sobra en este caso va 5 10 y sobra 2

print(suma)


# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5)) # Aqui str contierte un numero entero a string

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2 # Aqui al multiplicar de 5.0 y 5.0 es un float
print("Hola " * int(my_float)) # Aqui lo pasamos a entero



### Operadores Comparativos ###

igual_que = 5 == 6

distinto_de = 5 != 6

mayor_que = 5 > 6

menor_que = 5 < 6

mayor_o_igual = 5 >= 6

menor_o_igual = 5 <= 6

print(igual_que)


# Operaciones con cadenas de texto

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")



### Operadores Lógicos ###

# AND devuelve Falso si con una o dos son falsos

Resulado = True & True # Devuelve True
Resulado2 = False & True # Devuelve Falso
Resulado3 = True & False # Devuelve Falso
Resulado4 = False & False # Devuelve Falso

# OR devuelve Falso solo si las dos son Falsos

Resulado5 = True | True # Devuelve True
Resulado6 = False | True # Devuelve True
Resulado7 = True | False # Devuelve True
Resulado8 = False | False # Devuelve Falso

# NOT invierte el valor

Resulad9 = not True # Devuelve Falso
Resulado10 = not False # Devuelve True

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))