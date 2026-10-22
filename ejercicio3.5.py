edad = int(input("Cuantos años tienes: "))
ingresos = float(input("Cuanto son tus ingresos mensuales: "))

if edad < 16:
    print("No tienes la edad necesaria")
elif ingresos < 1000:
    print("No tienes los suficientes ingresos")
else:
    print("Cumples con todos los requisitos para tributar")