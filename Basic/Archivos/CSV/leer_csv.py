import csv

with open("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv",encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)