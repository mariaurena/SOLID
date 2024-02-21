
class Autenticacion:

    def __init__(self):
        self.nlibros = 0
        self.libros = []

    def registrar_libro(self, libro):
        self.libros.append(libro)
        self.nlibros += 1
        print("Libro '{}' registrado correctamente en la biblioteca".format(libro.get_titulo()))

    def baja_libro(self, libro):
        self.libros.remove(libro)
        print("Libro '{}' eliminado correctamente de la biblioteca".format(libro.get_titulo()))