"""Escribe un programa que solicite al usuario su año de nacimiento
y muestre en qué año cumplirá 18, 21 y 100 años.
"""

CURRENT_YEAR = 2026

ages = [18, 21, 100]

year_born = int(input("Ingrese el año en que nació: "))

for age in ages:
    year_age = age + year_born
    if year_age <= CURRENT_YEAR:
        print(f"Cumpliste {age} en el año {year_age}")
    else:
        print(f"Cumplirás {age} en el año {year_age}")