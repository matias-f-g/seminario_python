""" Escribe un programa que solicite al usuario una lista de palabras.
Luego, construí una oración uniendo únicamente las palabras que tengan
más de 3 letras, separadas por espacios. Las palabras cortas deben ser
excluidas del resultado final.
"""


words_list = input("Ingrese una lista de palabras: ").split()

words_selection = " ".join(w for w in words_list if len(w) > 3)

print(words_selection)



# # Long version
# 
# words_list = input("Ingrese una lista de palabras: ").split()
# 
# words_selection = ""
# 
# for w in words_list:
#     if len(w) > 3:
#         words_selection += " " + w
# 
# words_selection = words_selection.strip()
# 
# print(words_selection)

