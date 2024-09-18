import os

# 2 listas, una con nombres otra con apellidos

nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","Tarado"]

# Registrar esta informacion en un TXT de forma óptima

with open("D:/Programacion/Curso de Python/Basic/Archivos/Problemas/problema1.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    # La función zip en Python se utiliza para combinar dos o más iterables (listas, tuplas, etc.)
    [arch.writelines(f"Nombre: {n}\n Apellido {a}\n----------\n") for n,a in zip(nombres,apellidos)]


# Esto  [arch.writelines(f"Nombre: {n}\n Apellido {a}\n----------\n") for n,a in zip(nombres,apellidos)]  es lo mismo que esto:

#   for n,a in zip(nombres,apellidos):
#       arch.writelines(f"Nombre: {n}\n Apellido {a}\n----------\n")


# Ejemplo de uso de zip
# Definir dos listas
# nombres = ['Juan', 'María', 'Carlos']
# edades = [25, 30, 22]

# Combinar listas usando zip
# combinacion = zip(nombres, edades)

# Convertir el resultado a una lista
# resultado = list(combinacion)

# Imprimir el resultado
# Resultado: [('Juan', 25), ('María', 30), ('Carlos', 22)]
# print(resultado)