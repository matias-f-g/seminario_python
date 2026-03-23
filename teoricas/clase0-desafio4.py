char = input("Ingrese un carácter: ")

quotation_marks = ("\"", "\'")

if char in quotation_marks:
    print("Ingresaste una comilla")
else:
    print("No ingresaste una comilla")