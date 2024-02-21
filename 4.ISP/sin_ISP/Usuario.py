# simulación de lo que sería la interfaz Usuario
from abc import ABC, abstractmethod

class Usuario(ABC):

    @abstractmethod
    def iniciar_sesion(self, username, password):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass

    @abstractmethod
    def ver_contenido(self):
        pass

    @abstractmethod
    def editar_perfil(self):
        pass