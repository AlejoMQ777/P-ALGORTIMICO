num1 = int(input("introduce el primer número"))
num2 = int(input("introduce el segundo número"))

operador = input("introduce la operación a realizar(suma, resta, multiplicación, división, módulo): ")
if operador == "suma":
  resultado = num1 + num2
elif operador == "resta":
  resultado = num1 - num2
elif operador == "multiplicación":
  resultado = num1 * num2 
elif operador == "división":
  resultado = num1/num2
elif operador == "módulo":
  resultado = num1 % num2
  
  print("el resultado es", resultado)