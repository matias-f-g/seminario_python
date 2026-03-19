""" Modifica el ejercicio 4 para que, en lugar de imprimir los números,
genere dos listas: una con los múltiplos de 5 y otra con el
resto de los números. Imprimí ambas listas al finalizar.
"""

number = int(input("\nIngrese un número: "))

numbers = []
multiples = []

for i in range(1, number+1):
    multiples.append(i) if i % 5 == 0 else numbers.append(i)

print(f"\nSe imprimen los números del 1 al {number} (sin los múltiplos de 5):")

print(*numbers, sep='  ')

print(f"\nSe imprimen los múltiplos de 5 en ese mismo rango:")

print(*multiples, sep='  ')



# # Long version:
# 
# 
# number = int(input("\nIngrese un número: "))
# 
# numbers = []
# multiples = []
# 
# for i in range(1, number+1):
#     if i % 5 == 0:
#         multiples.append(i)
#     else:
#         numbers.append(i)
# 
# print(f"\nSe imprimen los números del 1 al {number} (sin los múltiplos de 5):")
# 
# for n in numbers:
#     print(n, end='  ')
# 
# print(f"\n\n\nSe imprimen los múltiplos de 5 en ese mismo rango")
# 
# for m in multiples:
#     print(m, end='  ')
# 
# print()
