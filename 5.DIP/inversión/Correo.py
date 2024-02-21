from Envio import Envio

class Correo(Envio):

    def enviar(self, informe):
        print("Enviando informe por correo: ", informe)