producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

total = precio * unidades

print(f"{producto}: {precio:.2f}€ x {unidades} unidades = {total:.2f}€")