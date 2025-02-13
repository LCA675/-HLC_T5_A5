class Persona:
    def __init__(self, nombre,edad, profesion):
        self.nombre=nombre
        self.edad=edad
        self.profesion=profesion

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y soy {self.profesion}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado=grado

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y estudio {self.grado}")

persona=Persona("Laura", 19, "Informática")
persona.presentarse()

estudiante=Estudiante("Laura", 19, "Informática","2 de SMR")
estudiante.presentarse()