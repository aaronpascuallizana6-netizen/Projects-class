# Ejercicio 4.2 Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Cuantos años tienes: "))

for a in range (edad):
    print(f"Has cumplido {a+1} años")