# Ejercicio 4.5 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("Cuanto dinero quieres invertir: "))
intereses = float(input("Cuantos intereses tienes: "))
years = int(input("Cuanto años quieres invertir: "))

for a in range(years):
    cantidad *= 1 + intereses / 100
    print(f"Dinero despues {str(a+1)} años: {str(round(cantidad, 2))}")