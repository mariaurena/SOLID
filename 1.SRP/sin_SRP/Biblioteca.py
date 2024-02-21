
class Biblioteca:

    def __init__(self):

        self.nlibros = 0
        self.libros  = []

    # ------- GET -------

    def get_nlibros(self):

        return self.nlibros

    def get_libros(self):

        if not self.libros:
            print("No hay libros registrados en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros:
                print("- Título:", libro.get_titulo())
                print("  Autor:", libro.get_autor())
                print("  Género:", libro.get_genero())
                print("  Número de copias:", libro.get_ncopias())
                print() 

    # ------- SET -------

    def set_nlibros(self, nuevos_nlibros):

        self.nlibros = nuevos_nlibros

    # ------- MÉTODOS -------

    def registrar_libro(self, libro):

        self.libros.append(libro)
        self.nlibros += 1
        print("Libro '{}' registrado correctamente en la biblioteca".format(libro.get_titulo()))

    def baja_libro(self, libro):
        self.libros.remove(libro)
        print("Libro '{}' eliminado correctamente de la biblioteca".format(libro.get_titulo()))
        
    # buscar libro por su titulo
    def buscar_por_titulo(self, titulo):

        for libro in self.libros:
            if libro.get_titulo() == titulo:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(titulo))
                return libro
        return None
    
    # buscar libro por su autor
    def buscar_por_autor(self, autor):

        for libro in self.libros:
            if libro.get_autor() == autor:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(libro.get_titulo()))
                return libro
        return None
    
    

