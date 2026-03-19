import random

CANT_RONDAS = 3

words = {
    "programación":[
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
],  "bandas":[
    "nirvana",
    "megadeth",
    "radiohead",
    "intoxicados"
], "películas":[
    "interestelar",
    "memento",
    "matrix",
    "oppenheimer",
    "tenet",
    "django"
]
}


print("\n_ _ _ _ _ ¡Bienvenido al Ahorcado! _ _ _ _ _\n")

while True:
    category = input("""Elija alguna de las siguientes categorías:
                        
        - programación
        - bandas
        - películas
                        
Su opción: """).lower()
    if category in words:
        print()
        break
    else:
        print("\nDebe ingresar el nombre de la categoría, tal como aparece en pantalla.\n")


# Se crea una lista con CANT_RONDAS palabras distintas elegidas de forma random de la categoría seleccionada
chosen_words = random.sample(words[category], CANT_RONDAS)

for i in range(CANT_RONDAS):
    word = chosen_words[i]
    guessed = []
    attempts = 6

    print(f"- - - - - Empieza la ronda número {i+1} - - - - -\n")

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print(f"¡Ganaste! Finalizaste la ronda con un puntaje de {attempts} puntos\n\n")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()
        if len(letter) != 1:
            print("Entrada no válida. Tenés que ingresar exactamente una letra.\n")
            continue
        elif not letter.isalpha():
            print("Entrada no válida. Tenés que ingresar una letra, no números ni caracteres especiales.\n")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
        print()

    if attempts == 0:
        print(f"¡Perdiste! Tu puntaje es 0. La palabra era: {word}\n")