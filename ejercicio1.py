class Persona:
    def __init__(self, nombre,edad, profesion):
        self.nombre=nombre
        self.edad=edad
        self.profesion=profesion

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y soy {self.profesion}")

persona=Persona("Laura", 19, "Informática")
persona.presentarse()