from abc import ABC, abstractmethod

class Envio(ABC):

    @abstractmethod
    def enviar(self, informe):
        pass
