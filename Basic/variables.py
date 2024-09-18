name = "Sebas"
print(name)
print(10 + 10)

numero = 10
numero += 5
numero -= 5
print(numero) 

# concatenar con +
nombre2 = "Sebas"
bienvenida = "Hola " + nombre2
print(bienvenida)

# concatenar con f-strings
nombre3 = "Sebastian"
bienvenida = f"Hola {nombre3}"
print(bienvenida)

nombre4 = "Sebastian"
bienvenida = f"Hola {nombre4}"
# Operadores de pertenencia (in / not in)
print("Sebastian" in bienvenida) # True
print("Sebastian" not in bienvenida) # False

x = 100
#case sensitive
book = "EL universo elegante"
Book = "Historia del Tiempo"


x,book = 100, "Relatividad General"
print(x)
print(book)

#Convenciones
book_name = "Relatividad General" #Snake Case
bookName = "Cien Años de Soledad" #Camel Case
BookName = "AEIOU" #Pascal Cas