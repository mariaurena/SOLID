from Correo import Correo
from Fax import Fax

from GeneradorInforme import GeneradorInforme   

# ahora generador de informe recibe una especificacion del envio
# (correo) pero en un futuro podría recibir cualquier otro tipo 
# de envio

correo = Correo()
generador_informe = GeneradorInforme( correo )
generador_informe.generar_informe()

# por ejemplo el envio por fax

fax = Fax()
generador_informe = GeneradorInforme( fax )
generador_informe.generar_informe()