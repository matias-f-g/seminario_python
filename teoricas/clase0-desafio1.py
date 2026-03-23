# Classic version

number = int(input("Ingrese un número entero: "))

if number % 2 == 0:
    print("Es par")
else:
    print("No es par")


# Pythonic version

number = int(input("Ingrese un número entero: "))

print("Es par") if number % 2 == 0 else print("No es par")

