class Persona:
    def __init__(self, nombre,edad, profesion):
        self.nombre=nombre
        self.edad=edad
        self.profesion=profesion

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y soy {self.profesion}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa=empresa

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y soy {self.profesion} y trabajo en {self.empresa}")

persona=Persona("Laura", 19, "Informática")
persona.presentarse()

trabajador=Trabajador("Laura",19 , "Informática", "NTTDATA")
trabajador.presentarse()