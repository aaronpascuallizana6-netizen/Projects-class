# Calcula el importe total que se debe por las horas trabajadas.
# Primero pedimos las horas trabajadas y el precio por hora.
# Después multiplicamos ambos valores para obtener el total.
horastrabajadas = float(input("¿Cuántas horas has trabajado? \n"))  # Pide las horas trabajadas.
print(f"Ha trabajado {horastrabajadas} horas")  # Muestra las horas introducidas.

costehoras = float(input("¿Cuánto vale cada hora? \n"))  # Pide el precio de cada hora.
print(f"Cada hora cuesta {costehoras}$")  # Muestra el precio por hora.

tedeben = horastrabajadas * costehoras  # Calcula el total a pagar.

print(f"Te deben un total de {tedeben}$")  # Muestra el resultado final