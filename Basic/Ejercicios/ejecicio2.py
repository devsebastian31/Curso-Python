# Crear una funcion que muestre la serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
    a,b = 0,1 # Variables
    fibonacci_lista = [0] # Inicia desde el 0
    for i in range(num): # Bucle for que ejecuta código para cada elemento icrementando en la lista y se ejecuta el bucle el numero de num
        if b > num: # Verifica si b es mayor que num si no lo es se ejecuta else 
            return fibonacci_lista # Si b es mayor que num estonces devuelve la lista desde el 0
        else:
            fibonacci_lista.append(b) # Agrega un nuevo elemento a la lista fibonacci
            a,b = b,a+b
            # a tomará el valor de b (1) y b tomará los valores antes del bucle for de a y b (0+1=1) y asi va sucesivamente en bucle

resultado = fibonacci(20)
print(resultado)