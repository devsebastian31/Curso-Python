# Abrimos el archivo
archivo_sin_leer = open("D:/Programacion/Curso de Python/Basic/Archivos/TXT/leer.txt",encoding="UTF-8") # encoding UTF-8 sirve para leer todos los caracteres

# leer archivo completo
# archivo = archivo_sin_leer.read() Leemos el archivo con read

# Leer por lineas
# lineas = archivo_sin_leer.readlines()

# leer una sola linea
linea = archivo_sin_leer.readline() # Si quieres leer hasta cierta parte debes poner el numero hasta que elemento quieres leer

# Cerrar el archivo
archivo_sin_leer.close()

# print(archivo)
print(linea)