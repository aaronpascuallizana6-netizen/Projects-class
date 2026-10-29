# Ejercicio 4.3 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Dime un numero: "))

for a in range(1, numero+1, 2):
    print(a, end=", ")