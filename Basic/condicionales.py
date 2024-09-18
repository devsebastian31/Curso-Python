edad = 16

if edad >= 18: # Si se cumple esta accion se ejecutara si no se ejecuta else
    print("Puedes pasar")
else:
    print("No puedes pasar, eres menor de edad")


usuario = "Sebastian"
base_de_datos = "Sebastian"

if usuario == base_de_datos:
    print("Iniciando Secion")
else:
    print("Usuario incorrecto")


# if anidados y else if (elif)
ingreso_mensual = int(input("Inserte su fondo: ")) # int sirve apra convertir un numero a entero
gasto_mensual = int(input("Inserte su gasto: "))

if ingreso_mensual > 10000: # En caso de que no se cumpla esta condicion pasa a la siguiente
    if ingreso_mensual - gasto_mensual > 2000:
        print("Fondo recomendado")
    else:
        print("Fondo normal")

elif ingreso_mensual >= 500: # Esta condicion se ejecuta si if no se cumple
    print("Fondo minimo")

else:
    print("Fondo insuficiente")