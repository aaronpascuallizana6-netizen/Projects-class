texto = input("Introduce números separados por comas (ej: 4, 8, 10): ")

numeros = []
for trozo in texto.split(','):
    numeros.append(int(trozo))

suma_total = sum(numeros)
cantidad = len(numeros)
media = suma_total / cantidad

suma_cuadrados = 0
for num in numeros:
    suma_cuadrados += (num - media) ** 2

desviacion = (suma_cuadrados / cantidad) ** 0.5

print(f"La media es {media}, y la desviación típica es {desviacion}")