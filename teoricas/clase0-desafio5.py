str1 = input("Ingrese una cadena: ")
str2 = input("Ingrese otra: ")

if len(str1) > len(str2):
    print(str1)
elif len(str1) < len(str2):
    print(str2)
else:
    print("Ambas tienen la misma cantidad de caracteres")