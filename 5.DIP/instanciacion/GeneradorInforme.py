from Correo import Correo

class GeneradorInforme:

    def __init__(self):
        # instanciamos la clase Correo
        self.correo = Correo()


    def generar_informe(self):

        informe = "Esto es un informe generado"

        self.correo.enviar( informe )

