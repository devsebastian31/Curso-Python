# Leer txt optimamente

# Modos de apertura:

# Modo de lectura (read): "r"
#   - Abre el archivo para lectura.
#   - Produce un error si el archivo no existe.


# Modo de escritura (write): "w"
#   - Abre el archivo para escritura.
#   - Sobrescribe el contenido existente si el archivo ya existe.
#   - Crea un nuevo archivo si no existe.


# Modo de adición (append): "a"
#   - Abre el archivo para escritura.
#   - Agrega contenido al final del archivo sin sobrescribir lo existente.
#   - Crea un nuevo archivo si no existe.


# Modo binario: "b"
#   - Abre el archivo en modo binario para leer o escribir bytes.
#   - Puede combinarse con "r", "w" o "a".


# Modo de exclusión: "x"
#   - Crea un nuevo archivo y lo abre para escritura.
#   - Produce un error si el archivo ya existe.


# Modo de texto (predeterminado): "t"
#   - Utilizado para abrir archivos de texto.
#   - Puede combinarse con "r", "w" o "a".


# Modo de actualización: "+"
#   - Permite lectura y escritura simultáneas.
#   - Puede combinarse con "r", "w" o "a".

# Estos modos se pueden combinar según sea necesario. 
# Por ejemplo, "rb" indica abrir un archivo en modo de lectura binaria

with open("D:/Programacion/Curso de Python/Basic/Archivos/TXT/leer.txt",encoding="UTF-8") as archivo: # Se abre en modo lectura
    # Se ejecuta solo si se abrio correctamente el archivo
    contenido = archivo.read()
    print(contenido)



# Escribir archivo TXT

# w sirve para escritura, si no encuentra el archivo, lo crea
with open("D:/Programacion/Curso de Python/Basic/Archivos/TXT/escribir.txt","w",encoding="UTF-8") as archivo:
    # Sobreescribir archivo
    # archivo.write("Esto esta escrito")
    
    # writelines se utiliza para escribir una lista de cadenas en un archivo
    archivo.writelines(["- Que tal\n", "- Hola\n"]) # Dejar espacio en lineas \n

    # agregando otras 2 lineas
    archivo.writelines(["- Bien y tu\n", "- y que haces"])

# a sirve para agregar líneas adicionales sin sobrescribir el contenido existente
with open("D:/Programacion/Curso de Python/Basic/Archivos/TXT/escribir.txt","a",encoding="UTF-8") as archivo:

    # Bucle for para agregar varias lineas
    for i in range(5):
        archivo.writelines(f"Linea {i+1} agregada\n")