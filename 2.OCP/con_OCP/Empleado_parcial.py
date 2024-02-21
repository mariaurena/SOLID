from Empleado import empleado

class empleado_parcial(empleado):

    def __init__(self):
        self.jornada = 6
        self.euros_hora = 12

    def calcular_sueldo(self):
        return self.jornada * self.euros_hora