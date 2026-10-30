# Ejercicio 4.8 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for a in range(1, numero+1, 2):
    for b in range(a, 0, -2):
        print(b, end=" ")
    print("")