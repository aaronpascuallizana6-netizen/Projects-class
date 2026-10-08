numero = input("Dime tu numero de telefono con los el prefijo y la extension: ")
resultado = numero[2:-2]
print("Tu numero de telefono es: " + resultado)
# while True:
#     entrada = input("Introduce un número de 13 dígitos: ")
    
#     # Comprueba que solo contenga dígitos y tenga máximo 13 de longitud
#     if entrada.isdigit() and len(entrada) <= 13:
#         break
#     else:
#         print("Error: Debe contener solo dígitos y un máximo de 13 caracteres.\n")

# # Aplicamos el corte eliminando los 2 primeros y 2 últimos
# resultado = entrada[2:-2]
# print("Resultado:", resultado)