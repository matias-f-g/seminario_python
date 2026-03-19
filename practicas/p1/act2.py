"""Escribe un programa que solicite al usuario una cantidad de segundos
y muestre cuántas horas, minutos y segundos equivalen.
Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.
"""

seconds = int(input("Ingrese una cantidad de segundos: "))

hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60

print(f"Equivale a {hours} hora(s), {minutes} minuto(s) y {seconds} segundo(s)")


# # Another possible solution:
# 
# import datetime
# 
# seconds = int(input("Ingrese una cantidad de segundos: "))
# 
# print(datetime.timedelta(seconds=seconds))


