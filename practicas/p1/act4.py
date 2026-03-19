""" Crea un programa que dado un número N ingresado por el usuario, imprima
los números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la
sentencia continue donde haga falta.
"""

number = int(input("Ingrese un número: "))

print(f"\nEstos son los números del 1 al {number}, sin los múltiplos de 5\n")

print([i for i in range(1, number+1) if i % 5 != 0])



# # Another option:
# 
# for i in range(1, number+1):
#     if i % 5 == 0:
#         continue
#     print(i)