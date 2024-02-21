class Busqueda:

    def __init__(self, autenticacion):
        self.autenticacion = autenticacion

    def buscar_por_titulo(self, titulo):
        libros_registrados = self.autenticacion.libros
        for libro in libros_registrados:
            if libro.get_titulo() == titulo:
                print("Libro '{}' encontrado correctamente en la biblioteca".format(titulo))
                return libro
        print("Libro '{}' no encontrado en la biblioteca".format(titulo))
        return None

    def buscar_por_autor(self, autor):
        libros_registrados = self.autenticacion.libros
        for libro in libros_registrados:
            if libro.get_autor() == autor:
                print("Libro del autor '{}' encontrado correctamente en la biblioteca".format(autor))
                return libro
        print("No se encontraron libros del autor '{}' en la biblioteca".format(autor))
        return None
    
    def get_libros(self):
        libros_registrados = self.autenticacion.libros
        if not libros_registrados:
            print("No hay libros registrados en la biblioteca.")
        else:
            print("Lista de libros en la biblioteca:")
            for libro in libros_registrados:
                print("- Título:", libro.get_titulo())
                print("  Autor:", libro.get_autor())
                print("  Género:", libro.get_genero())
                print("  Número de copias:", libro.get_ncopias())
                print() 