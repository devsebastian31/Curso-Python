from math import pi as PI_VALUE
import math
# En caso de que el fichero este dentro de una carpeta se debe primero acceder a la carpeta y luego al fichero  carpeta.my_module
from my_module import sumValue, printValue # Importamos el modulo seguido de la funcion del fichero
import my_module # Importamos el fichero para poder acceder a my_module.py

my_module.sumValue(5, 3, 1) # Accedemos a los datos que tiene el modulo my_module
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python") # Llamamos a la funcion


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)