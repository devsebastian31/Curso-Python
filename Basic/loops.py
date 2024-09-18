foods = ["apples", "bread", "cheese", "milk", "bananas", "xd"]

# El bucle for ejecuta un bloque de código para cada elemento en la secuencia de dicho objeto
# El bucle for recorre cada uno de los alimentos en la lista
for food in foods:
    if food == "milk":
        print("Compra esto")
        break # breack termina con el bucle
    print(food)


# El bucle for recorre cada uno de los alimentos en la lista
for food in foods:
    if food == "milk":
        print("En milk se salta y continua con el bucle")
        continue # continue se salta una parte del bucle si se cumple una determinada condición.
    print(food)


for number in range(1, 8): # number es cada una de los items de este rango
    print(number)


count = 4

while count <= 10: # while se ejecuta infinitamente si count es menor o igual a 10
    print(count)
    count = count + 1 # Al sumarse 1 y llegar a 10 termina el bucle