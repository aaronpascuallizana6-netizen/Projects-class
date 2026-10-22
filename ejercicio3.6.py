nombre = input("Cual es tu nombre: ")
sexo = input("Cual es tu sexo (M o H): ")

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() < "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es ", grupo)