"""Crea un programa que solicite al usuario un número y muestre
su tabla de multiplicar del 1 al 10 utilizando un bucle for.
"""

number = int(input("Ingrese un número: "))

print(f"\nAsí es la tabla del {number}\n")

for i in range(1, 11):
    print(i , "-->", number * i)