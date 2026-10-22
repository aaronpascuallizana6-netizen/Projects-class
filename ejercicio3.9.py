edad = int(input("Que edad tienes: "))

if edad < 4:
    print("Tu entrada es gratuita")

elif edad >= 4 and edad < 18:
    print("Tu entrada cuesta 5$")

else:
    print("Tu entrada cuesta 10$")