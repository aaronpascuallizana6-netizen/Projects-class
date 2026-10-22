print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")

pregunta = input("Deseas pizza vegetariano o no vegetariano: ")

if pregunta == "1":
    print("Has elegido la opción vegetariana. Los ingredientes son pimiento y tofu.")

elif pregunta == "2":
    print("Has elegido la opcion no vegetariano. Los ingrediente son peperoni, jamón y salmón")

else:
    print("Opcion no válida.")