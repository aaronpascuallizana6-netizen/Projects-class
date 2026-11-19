palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocales in vocales: 
    times = 0
    for letter in palabra: 
        if letter == vocales:
            times += 1
    print("La vocal " + vocales + " aparece " + str(times) + " veces")