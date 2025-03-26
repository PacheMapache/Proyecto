#Crea un programa con 3 clases: La primera debe llamarse "Universidad" y ahí se guardará el nombre 
# de la universidad. La segunda clase se llamará "Carrera" con un atributo llamado "Especialidad" (donde se
# guarda el nombre de la especialidad estudiada por un estudiante, y finalmente crea una clase llamada "Estudiante")
# que contenga los atributos "nombre" y "edad". El programa debe imprimir la especialidad, la edad, el nombre
# y el nombre de la universidad del estudiante con un objeto llamado "persona"

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def mostrarinfo(self):
        print("Especialidad: ", self.carrera.especialidad)
        print("Edad: ", self.edad)
        print("Nombre: ", self.nombre)
        print("Universidad: ", self.universidad.nombre)

#Ingresamos datos al código para comprobar su funcionamiento

#Creamos el nombre de la universidad
universidad = Universidad("Uniminuto")

#Creamos la facultad
carrera = Carrera("Tecnología en Desarrollo de Software")

#Creamos un estudiante y sus atributos
persona = Estudiante("El Coteño", 19, universidad, carrera)

#Mostramos todo
persona.mostrarinfo()