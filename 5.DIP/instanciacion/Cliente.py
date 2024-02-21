from GeneradorInforme import GeneradorInforme

# el cliente desconoce la dependencia de GeneradorInforme
generadorInforme = GeneradorInforme()

generadorInforme.generar_informe()

# al hacer un test no sabemos qué correos poseen los informes
# por tanto tendríamos que consultarlos (pueden estar en una bd)