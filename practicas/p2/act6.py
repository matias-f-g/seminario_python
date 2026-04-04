"""Dadas las siguientes publicaciones de una red social, extraiga todos los
hashtags (palabras que comienzan con #), cuente la frecuencia de cada uno, y
muestre los hashtags trending (los que aparecen más de una vez).
"""

# Counter: es una colección desordenada de pares claves-valor, donde las claves
# son los elementos de la colección y los valores son la cantidad de ocurrencias de los mismos.

from collections import Counter


posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

all_hastag_words = []

for post in posts:
    all_hastag_words += list(filter(lambda w : w.startswith("#"), post.split()))

hastags_count = Counter(all_hastag_words)

print("\nHashtags trending (más de una aparición):")
for hastag, count in hastags_count.items():
    if count > 1:
        print(f"{hastag}: {count}")

print("\nTotal de hashtags únicos: ", len(hastags_count))



# # My first solution was:
# 
# hastags_count = {}
# 
# for post in posts:
#     words = post.split()
#     hastag_words = list(filter(lambda w : w.startswith("#"), words))
#     for hw in hastag_words:
#         hastags_count[hw] = hastags_count.setdefault(hw, 0) + 1
