from Autenticacion import Autenticacion
from Busqueda import Busqueda
from Libro import Libro


autenticacion = Autenticacion()
busqueda      = Busqueda(autenticacion)

# Registrando libros
libro1 = Libro("El nombre del viento", "Patrick Rothfuss", "Fantasia", 6)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 4)
autenticacion.registrar_libro(libro1)
autenticacion.registrar_libro(libro2)

# Búsqueda
busqueda.get_libros()
busqueda.buscar_por_titulo("El nombre del viento")
busqueda.buscar_por_autor("Gabriel García Márquez")



