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
#codigo numero 1 de la hoja del laboratorio  10



class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos_basicos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def calcular_dosis(self, medicamento, dosis_por_kg):
        return self.peso * dosis_por_kg

    def generar_ficha_medica(self, motivo_consulta, diagnostico):
        print("\n--- Ficha Médica ---")
        self.mostrar_datos_basicos()
        print(f"Raza: {self.raza}")
        print(f"Motivo de la consulta: {motivo_consulta}")
        print(f"Diagnóstico: {diagnostico}")
        print("----------------------")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color_pelo):
        super().__init__(nombre, edad, peso)
        self.color_pelo = color_pelo

    def calcular_dosis(self, medicamento, dosis_por_kg):
        # Dosis ligeramente diferente para gatos (ejemplo)
        return self.peso * (dosis_por_kg * 0.8)

    def generar_ficha_medica(self, motivo_consulta, diagnostico, necesita_vacuna_rabia=False):
        print("\n--- Ficha Médica ---")
        self.mostrar_datos_basicos()
        print(f"Color de pelo: {self.color_pelo}")
        print(f"Motivo de la consulta: {motivo_consulta}")
        print(f"Diagnóstico: {diagnostico}")
        if necesita_vacuna_rabia:
            print("Necesita vacuna contra la rabia.")
        print("----------------------")

class Ave(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

    def calcular_dosis(self, medicamento, dosis_por_kg):
        # Dosis para aves (ejemplo)
        return self.peso * (dosis_por_kg * 0.5)

    def generar_ficha_medica(self, motivo_consulta, diagnostico, envergadura_alas):
        print("\n--- Ficha Médica ---")
        self.mostrar_datos_basicos()
        print(f"Especie: {self.especie}")
        print(f"Envergadura de alas: {envergadura_alas} cm")
        print(f"Motivo de la consulta: {motivo_consulta}")
        print(f"Diagnóstico: {diagnostico}")
        print("----------------------")

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, tipo_sangre_fria):
        super().__init__(nombre, edad, peso)
        self.tipo_sangre_fria = tipo_sangre_fria

    def calcular_dosis(self, medicamento, dosis_por_kg):
        # Dosis para reptiles (ejemplo)
        return self.peso * (dosis_por_kg * 0.2)

    def generar_ficha_medica(self, motivo_consulta, diagnostico, temperatura_ambiente_optima):
        print("\n--- Ficha Médica ---")
        self.mostrar_datos_basicos()
        print(f"Tipo de sangre: {self.tipo_sangre_fria}")
        print(f"Temperatura ambiente óptima: {temperatura_ambiente_optima} °C")
        print(f"Motivo de la consulta: {motivo_consulta}")
        print(f"Diagnóstico: {diagnostico}")
        print("----------------------")

# Ejemplo de uso
perrito = Perro("Max", 3, 15, "Golden Retriever")
gatito = Gato("Luna", 2, 4, "Siamesa")
pajarito = Ave("Piolín", 1, 0.2, "Canario")
reptilito = Reptil("Coco", 5, 2, "Poiquilotermo")

perrito.mostrar_datos_basicos()
dosis_perro = perrito.calcular_dosis("Amoxicilina", 10)
print(f"Dosis de Amoxicilina para {perrito.nombre}: {dosis_perro} mg")
perrito.generar_ficha_medica("Tos y estornudos", "Posible resfriado")

gatito.mostrar_datos_basicos()
dosis_gato = gatito.calcular_dosis("Enrofloxacina", 5)
print(f"Dosis de Enrofloxacina para {gatito.nombre}: {dosis_gato} mg")
gatito.generar_ficha_medica("Vómitos ocasionales", "Sospecha de indigestión", necesita_vacuna_rabia=True)

pajarito.mostrar_datos_basicos()
dosis_ave = pajarito.calcular_dosis("Doxiciclina", 20)
print(f"Dosis de Doxiciclina para {pajarito.nombre}: {dosis_ave} mg")
pajarito.generar_ficha_medica("Plumas erizadas", "Posible infección respiratoria", envergadura_alas=15)

reptilito.mostrar_datos_basicos()
dosis_reptil = reptilito.calcular_dosis("Ciprofloxacino", 8)
print(f"Dosis de Ciprofloxacino para {reptilito.nombre}: {dosis_reptil} mg")
reptilito.generar_ficha_medica("Letargo", "Posible baja temperatura", temperatura_ambiente_optima=28)



'''
_______Ejercicio_de_clases_2_______

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"DNI: {self.dni}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, numero_matricula, carrera):
        super().__init__(nombre, edad, dni)
        self.numero_matricula = numero_matricula
        self.carrera = carrera

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Matrícula: {self.numero_matricula}")
        print(f"Carrera: {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, numero_empleado, departamento, asignaturas):
        super().__init__(nombre, edad, dni)
        self.numero_empleado = numero_empleado
        self.departamento = departamento
        self.asignaturas = asignaturas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Empleado: {self.numero_empleado}")
        print(f"Departamento: {self.departamento}")
        print(f"Asignaturas: {', '.join(self.asignaturas)}")

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, puesto, antiguedad):
        super().__init__(nombre, edad, dni)
        self.puesto = puesto
        self.antiguedad = antiguedad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puesto: {self.puesto}")
        print(f"Antigüedad: {self.antiguedad} años")

# Ejemplo de uso
estudiante1 = Estudiante("Ana Pérez", 20, "12345678A", "S1001", "Ingeniería Informática")
profesor1 = Profesor("Carlos López", 45, "98765432B", "P205", "Informática", ["Programación I", "Estructuras de Datos"])
administrativo1 = Administrativo("Laura Gómez", 35, "55555555C", "Secretaria", 5)

print("--- Información del Estudiante ---")
estudiante1.mostrar_informacion()

print("\n--- Información del Profesor ---")
profesor1.mostrar_informacion()

print("\n--- Información del Administrativo ---")
administrativo1.mostrar_informacion()
'''



