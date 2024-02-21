from GeneradorInforme import GeneradorInforme
from Correo import Correo

# el cliente conoce la dependencia de GeneradorInforme
correo = Correo()
generadorInforme = GeneradorInforme( correo )

generadorInforme.generar_informe()

# al hacer un test ya sabemos qué dependencias posee
# el generador de informe por tanto no tenemos que ir a consultarlas 