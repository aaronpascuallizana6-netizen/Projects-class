# Programa que calcula la suma de los números desde 1 hasta n.
# La fórmula usada es: n * (n + 1) / 2

numero = float(input("Ponga un numero: "))  # Guarda el número introducido por el usuario.
parentesis = numero + 1  # Calcula n + 1 para la fórmula.
multiplicacion = numero * parentesis  # Multiplica n por (n + 1).
division = multiplicacion / 2  # Divide el resultado entre 2.

print(division)  # Muestra el resultado final.