### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: # except se ejecuta cuando hay un error
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre pase lo que pase
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: # indica que ha recibido un argumento de tipo correcto, pero con un valor incorrecto
    print("Se ha producido un ValueError")
except TypeError: # indica que cierto tipo de dato no es compatible con el otro tipo de dato "10" + 5
    print("Se ha producido un TypeError")

# Captura de la información de la excepción (Sirve para saver por que da el error)

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # ValueError captura la información del error en una variable llamada error
    print(error)
except Exception as my_random_error_name: # Se ejecutará si se produce cualquier otro tipo de error que no sea de tipo ValueError
    print(my_random_error_name)


def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
            break
        except ValueError:
            if not a.isnumeric():
                print("Ingresaste una letra en numero 1")
            elif not b.isnumeric():
                print("Ingresaste una letra en numero 2")
            else:
                break
        finally: # Ejecuta todas las líneas sin importar si se levantó alguna excepción
            print("Esto se ejecuta siempre")
            
    return resultado
    
print(sumar_dos())


# clase llamada MiException que hereda de la clase base Exception
class MiException(Exception):
     # Constructor de la clase con un parámetro 'err' que representa el mensaje de error
    def __init__(self, err):
        # Imprime un mensaje indicando el error que se ha cometido
        print(f"Cometiste el siguiente error: {err}")

try:
    raise MiException("Este es un error") # raise sirve para lanzar excepciones
except:
    print("Como vas a cometir ese error")