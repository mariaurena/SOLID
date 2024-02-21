from Empleado import Empleado

empleado  = Empleado()

print("El sueldo de un empleado a tiempo parcial es:", empleado.calcular_salario("parcial"))
print("El sueldo de un empleado a tiempo completo es: ", empleado.calcular_salario("completo"))