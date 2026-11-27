valores1 = (1, 2, 3)
valores2 = (-1, 0, 2)
producto = 0
for i in range(len(valores1)):
    producto += valores1[i]*valores2[i]
print("El producto de los vectores" + str(valores1) + " y " + str(valores2) + " es " + str(producto))