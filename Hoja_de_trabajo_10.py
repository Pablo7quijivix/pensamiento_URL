'''
Trabajo en proceso dia de laboratorio, miercoles 30 de abril
Con base a la información, realiza las siguientes clases utilizando herencia.
1. Clínica veterinaria
• Clase base: Animal (nombre, edad, peso).
• Clases hijas: Perro, Gato, Ave y reptil. (atributos propios de la clase)
• Salidas:
o Mostrar datos médicos básicos.
o Calcular dosis de medicamentos según especie.
o Generar ficha médica.

'''

class Animal: 
    def __init__(self, nombre):
        self.nombre = nombre
        
class Perro(Animal):
    def __init__(self, raza, sexo):
        super ().__init__(nombre) #Llama al constructor del animal
        self.sexo = sexo
        self.raza = raza 
        
class Animal:
    def hablar (self):
        print ("hace un sonido ")
        
class Gato(Animal):
    def hablar(self):
        super().hablar(
            print ("Miu"))
