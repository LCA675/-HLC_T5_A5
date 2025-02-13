class Persona:
    def __init__(self):
        self.nombre=input("Introduce tu nombre: ")
        self.edad=input("Introduce tu edad: ")
        self.profesion=input("Introduce tu profesion: ")

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} y soy {self.profesion}")

persona=Persona()
persona.presentarse()