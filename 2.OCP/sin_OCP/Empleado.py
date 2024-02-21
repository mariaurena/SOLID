
class Empleado:

    def __init__(self):

        self.tipo       = "completo"
        self.jornada    = 0
        self.euros_hora = 0
    
    def calcular_salario(self, tipo): 

        if ( tipo == "parcial" ):
            self.jornada = 6
            self.euros_hora = 12

        elif ( tipo == "completo" ):
            self.jornada = 8
            self.euros_hora = 15

        return self.jornada * self.euros_hora
    


            

        