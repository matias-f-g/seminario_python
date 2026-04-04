
cost_by_zone = {"local" : [500, 1000, 2000],
                "regional" : [1000, 2500, 4500],
                "nacional" : [2000, 5000, 8000]
                }

weight = float(input("Ingrese el peso del paquete (en kg): "))

if weight < 1:
    type_of_weight = 0
elif weight <= 5:
    type_of_weight = 1
else:
    type_of_weight = 2

zone = input("Ingrese la zona de destino (local/regional/nacional): ")

if zone in cost_by_zone:
    print(f"Costo de envío: ${cost_by_zone[zone][type_of_weight]}")
else:
    print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
