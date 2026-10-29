# Ejercicio 4.6 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for a in range(numero):
    for j in range(a+1):
        print("*", end="")
    print("")