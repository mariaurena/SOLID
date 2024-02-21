from Usuario import Usuario

class GestionUsuario(Usuario):

    def __init__(self):
        self.username = ""
        self.password = ""

    def iniciar_sesion(self, username, password):
        self.username = username
        self.password = password
        print(f"Iniciando sesión como: {self.username}")

    def cerrar_sesion(self):
        print(f"Cerrando sesión de: {self.username}")

    def editar_perfil(self):
        print("Editando perfil")

    def ver_contenido(self):
        print("Viendo contenido")
