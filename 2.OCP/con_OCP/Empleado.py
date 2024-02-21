from abc import ABC, abstractmethod

class empleado(ABC):

    def __init__(self):
        self.jornada = 0
        self.euros_hora = 0

    @abstractmethod
    def calcular_sueldo(self):
        pass