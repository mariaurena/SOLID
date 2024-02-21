class GeneradorInforme:

    def __init__(self, correo):
        # inyectamos la clase Correo
        self.correo = correo


    def generar_informe(self):

        informe = "Esto es un informe generado"

        self.correo.enviar( informe )

