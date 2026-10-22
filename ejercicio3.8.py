puntuacion = float(input("Introduce tu puntuación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 2400 * puntuacion
    print("Tu nivel es:", nivel)
    print("Te corresponden:", dinero, "€")

elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
    print("Tu nivel es:", nivel)
    print("Te corresponden:", dinero, "€")

elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
    print("Tu nivel es:", nivel)
    print("Te corresponden:", dinero, "€")

else:
    print("Puntuación no válida.")