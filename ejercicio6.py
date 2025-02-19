class Libro():
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.biblio = []

    def añadir_libro(self, libro):
        self.biblio.append(libro)

    def mostrar_libros(self):
        for i, libro in enumerate(self.biblio,start=1):
            print(f"{i}.{libro.titulo}-{libro.autor}")

bibliote = Biblioteca()
bibliote.añadir_libro(Libro("George Orwell", "1984"))
bibliote.añadir_libro(Libro("Gabriel García Márquez", "Cien Años de Soledad"))
bibliote.mostrar_libros()
