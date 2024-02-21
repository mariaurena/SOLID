
class Libro:

    def __init__(self, titulo, autor, genero, ncopias):

        self.titulo  = titulo
        self.autor   = autor
        self.genero  = genero
        self.ncopias = ncopias

    # ------- GET -------

    def get_titulo(self):

        return self.titulo

    def get_autor(self):
        
        return self.autor

    def get_genero(self):
        
        return self.genero

    def get_ncopias(self):

        return self.ncopias

    # ------- SET -------
        
    def set_titulo(self, nuevo_titulo):

        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        
        self.autor = nuevo_autor

    def set_genero(self, nuevo_genero):
        
        self.genero = nuevo_genero

    def set_ncopias(self, nuevas_ncopias):
        
        self.ncopias = nuevas_ncopias