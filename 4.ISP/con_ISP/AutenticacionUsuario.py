# simulación de lo que sería la interfaz Usuario
from abc import ABC, abstractmethod

class AutenticacionUsuario(ABC):

    @abstractmethod
    def iniciar_sesion(self, username, password):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass