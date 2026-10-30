# Ejercicio 4.9 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

passwd = "hola"
usuario = input("Confirma contraseña: ")

while passwd != usuario:
    print("Contraseña incorrecta, vuelva a escribirla")
    usuario = input("Vuelva a escribirla: ")
        
print("Contraseña correcta")        