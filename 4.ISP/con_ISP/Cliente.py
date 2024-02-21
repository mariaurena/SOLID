from AutenticacionUsuario import AutenticacionUsuario

class Cliente(AutenticacionUsuario):

    def __init__(self):
        self.username = ""
        self.password = ""

    # sólo implementa los métodos que están relacionados
    # con la autenticación del usuario
        
    def iniciar_sesion(self, username, password):
        self.username = username
        self.password = password
        print(f"Iniciando sesión como: {self.username}")

    def cerrar_sesion(self):
        print(f"Cerrando sesión de: {self.username}")



cliente = Cliente()
cliente.iniciar_sesion("mariaurena","3457863")
cliente.cerrar_sesion()