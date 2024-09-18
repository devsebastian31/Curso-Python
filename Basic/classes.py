class MyEmptyPerson: # class son bloques de código que encapsulan datos y funciones relacionadas
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())


# Clase con constructor, funciones y popiedades privadas y públicas

class Person:
    def __init__(self, name, surname, alias="Sin alias"): # init al crear ya viene con self y se utiliza para inicializar objetos de una clase
        # Propiedad pública significa que se puede ejecutar desde afuera print(my_person.full_name)
        self.full_name = f"{name} {surname} ({alias})" # Aqui name y surname los almacena en full_name
        # Propiedad privada significa 
        self.__name = name # Aqui solo estamos llamando al name 

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando") # Aqui despues de almacenar name y surname en full_name la usamos en esta funcion


my_person = Person("Brais", "Moure") # Brais Moure (Sin alias)
print(my_person.full_name) # Brais
print(my_person.get_name()) # Brais Moure (Sin alias) está caminando
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev") # Brais Moure (MoureDev)
print(my_other_person.full_name)
my_other_person.walk() # Brais Moure (MoureDev) está caminando
my_other_person.full_name = "Héctor de León (El loco de los perros)" # Aqui ya declaramos name surname y alias por defecto todo
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)