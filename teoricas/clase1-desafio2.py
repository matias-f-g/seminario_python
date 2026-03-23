"""Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
aquellas que empiecen y terminen con la misma letra.

The program assumes that the user enters a maximum of one word.
"""


word = input("Ingrese una palabra: ")


while word != "FIN":

    # This first "if" avoids problems with empty strings
    if word:
        print(word if word[0] == word[-1] else "")
    
    word = input("Ingrese una palabra: ")