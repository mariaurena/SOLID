from Envio import Envio

class GeneradorInforme:

    def __init__(self, envio):
        self.envio = envio


    def generar_informe(self):

        informe = "Esto es un informe generado"

        self.envio.enviar( informe )

