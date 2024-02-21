from Empleado import empleado

class empleado_completo(empleado):

    def __init__(self):
        self.jornada = 8
        self.euros_hora = 15

    def calcular_sueldo(self):
        return self.jornada * self.euros_hora