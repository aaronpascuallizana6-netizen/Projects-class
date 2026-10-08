precio = (input("Dime el precio de un producto en euros, con los dos decimales: "))
precio_limpio = precio.replace("," , ".")
euros , centimos = precio_limpio.split(".")
# centimos = centimos.ljust(2, "0")[:2]
print(f"Son {euros} euros con {centimos} centimos")