asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for asignaturas in asignaturas:
    score = float(input("¿Qué nota has sacado en " + asignaturas + "?"))
    if score >= 5:
        passed.append(asignaturas)
for asignaturas in passed:
    asignaturas.remove(asignaturas)
print("Tienes que repetir " + str(asignaturas))