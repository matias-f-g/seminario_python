letter = input("Ingrese una letra: ")

if letter.isalpha():
    print("Es mayúscula") if letter.isupper() else print("Es minúscula")
else:
    print("No ingresaste una letra")