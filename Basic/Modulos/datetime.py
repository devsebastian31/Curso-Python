from datetime import timedelta
import datetime

print(datetime.date.today()) # Mostrar fecha

def Conversion(): # Creamos la funcion
    Conversion = timedelta(minutes=int(input("Ingrese los minutos a convertir en horas: "))) # Convertir minutos en horas
    if Conversion:
        print(Conversion)
    else:
        print("No se pudo obtener la conversion")

Conversion()


print()