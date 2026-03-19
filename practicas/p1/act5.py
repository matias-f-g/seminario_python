""" Escribe un programa que simule una caja registradora: el usuario
ingresa precios de productos de a uno. Cuando ingresa 0, el programa
se detiene y muestra el total acumulado.
Nota: utilizá la sentencia break cuando haga falta.
"""

total = 0

while True:
    price = float(input("Ingrese un precio: "))
    if price == 0:
        break
    total += price

print(f"El total es: {total}")



# # The classic solution would be:
# 
# total = 0
# 
# price = float(input("Ingrese un precio: "))
# 
# while price != 0:
#     total += price
#     price = float(input("Ingrese un precio: "))
# 
# print(f"El total es: {total}")
