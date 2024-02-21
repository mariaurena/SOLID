from Empleado_completo import empleado_completo
from Empleado_parcial  import empleado_parcial

empleado_parcial = empleado_parcial()
print("Salario empleado parcial:", empleado_parcial.calcular_sueldo())

empleado_completo = empleado_completo()
print("Salario empleado completo:", empleado_completo.calcular_sueldo())
