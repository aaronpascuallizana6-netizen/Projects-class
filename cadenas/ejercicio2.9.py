fecha = input("Dime tu fecha de nacimiento (dd/mm/aaaa): ")
fecha_limpia = fecha.replace("/" , ".")
dia , mes , anyo = fecha_limpia.split(".")
print(f"Naciste el dia {dia} del {mes} de {anyo}")