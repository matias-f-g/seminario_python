words = []

print("\nIngrese cuatro palabras\n")

for i in range(4):
    word = input(f"Ingrese la palabra N° {i+1}: ")
    words.append(word)

for word in words:
    if "r" in word:
        print(word)
