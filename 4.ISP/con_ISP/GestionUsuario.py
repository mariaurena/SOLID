# simulación de lo que sería la interfaz Usuario
from abc import ABC, abstractmethod

class GestionUsuario(ABC):

    @abstractmethod
    def ver_contenido(self):
        pass

    @abstractmethod
    def editar_perfil(self):
        pass