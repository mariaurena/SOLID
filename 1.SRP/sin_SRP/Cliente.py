from Biblioteca import Biblioteca
from Libro import Libro


biblioteca = Biblioteca()

libro1 = Libro("Harry Potter", "J.K.Rowling", "Fantasia", 6)
libro2 = Libro("La amiga estupenda", "Elena Ferrante", "Amistad", 2)
libro3 = Libro("Film for her", "Carloto", "Fotografia", 16)

biblioteca.registrar_libro(libro1)
biblioteca.registrar_libro(libro2)
biblioteca.registrar_libro(libro3)

biblioteca.get_libros()

biblioteca.buscar_por_titulo("La amiga estupenda")
biblioteca.buscar_por_autor("J.K.Rowling")



