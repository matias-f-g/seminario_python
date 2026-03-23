"""The program does more than expected, but it is easily scalable"""

number = int(input("Ingrese un número entero: "))

multiples = (2, 3, 5)
multiples_indeed = []

for m in multiples:
    if number % m == 0:
        print(f"El número es múltiplo de {m}")
        multiples_indeed.append(m)

if not multiples_indeed:
    print(f"El número ingresado no era múltiplo de ninguno de estos números: {multiples}")