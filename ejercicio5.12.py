matriz_a = [
    [1, 2, 3],
    [4, 5, 6]]

matriz_b = [
    [-1, 0],
    [0, 1],
    [1, 1]]

resultado = [
    [0, 0],
    [0, 0]]

for fila in range(2):
    for columna in range(2):
        for paso in range(3):
            resultado[fila][columna] += matriz_a[fila][paso] * matriz_b[paso][columna]

for fila in resultado:
    print(fila)