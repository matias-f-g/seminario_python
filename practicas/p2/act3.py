"""Dada la reseña de una película, solicite al usuario una lista de palabras
consideradas spoilers (separadas por coma).
El programa debe reemplazar todas las apariciones de esas palabras en el texto
por asteriscos (*) de la misma longitud, sin distinguir mayúsculas de minúsculas.
"""

import re

review = """La película sigue a un grupo de astronautas que viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo a través
de tormentas solares y fallos en el sistema de navegación. Al llegar
a Marte descubren que la base está abandonada y los suministros
destruidos. Torres decide sacrificar la nave nodriza para salvar
al equipo y logran volver a la Tierra en una cápsula de emergencia.
El final revela que Torres sobrevivió gracias a un pasaje secreto."""

# In the example, spoiler_words = Marte, Torres, sacrificar, sobrevivió

spoiler_words = input("Ingrese las palabras spoiler (separadas por coma): ").split(',')
spoiler_words = [word.strip() for word in spoiler_words]

# Build the regex pattern to search for any spoiler word, e.g. "Marte|Torres|etc."
pattern = '|'.join(re.escape(word) for word in spoiler_words)

# Replace each spoiler word found in the review with asterisks of the same length, case-insensitive.
censored = re.sub(pattern, lambda m: '*' * len(m.group()), review, flags=re.IGNORECASE)

print()
print(censored)



# # THIS WAS MY FISRT SOLUTION
# 
# # First, everything is converted to lowercase and the text is separated by commas into a list of words.
# spoiler_words = input("Ingrese las palabras spoiler (separadas por coma): ").casefold().split(',')
# 
# # Next, the remaining spaces are removed
# spoiler_words = [word.strip() for word in spoiler_words]
# 
# print()
# 
# for line in review.splitlines():
#     for word in line.split():
#         if word.strip(" .,").casefold() in spoiler_words:
#             word = "*" * len(word) # with a little bug here (it even converts special chars to *)
#         print(word, end=' ')
#     print()