"""Implemente el cifrado César, que consiste en desplazar cada letra del alfabeto
una cantidad fija de posiciones. El programa debe:

    1. Solicitar un mensaje al usuario.
    2. Solicitar un valor de desplazamiento (número entero).
    3. Mostrar el mensaje cifrado.
    4. Mostrar el mensaje descifrado a partir del cifrado (para verificar que funciona).

Las letras deben rotar (después de la Z viene la A). Los caracteres que no sean
letras (espacios, signos de puntuación, números) se mantienen sin cambios. Debe
funcionar tanto con mayúsculas como con minúsculas, preservando el formato original.
"""

# Works all right for english text, but if you introduce weird chars like 'ñ' or 'ó',
# you'll get into trouble!
# We assume your key is a valid number between 1 and 25.
 

def main():
    plain_text = input("\nIngrese un mensaje: ")
    cipher_key = int(input("Ingrese el desplazamiento: "))

    cipher_text = cipher(plain_text, cipher_key)
    dechiper_text = decipher(cipher_text, cipher_key)

    print(f"\nMensaje cifrado: {cipher_text}")
    print(f"Mensaje descifrado: {dechiper_text}")




def cipher(plain_text, cipher_key):
    cipher_text = ""

    for one_char in plain_text:
        if one_char.isalpha():
            if one_char.isupper(): # 65-90
                ascii_value = ord(one_char) + cipher_key
                if ascii_value > 90:
                    ascii_value = ascii_value - 26 
            else: # 97-122
                ascii_value = ord(one_char) + cipher_key
                if ascii_value > 122:
                    ascii_value = ascii_value - 26 
            cipher_text += chr(ascii_value)
        else:
            cipher_text += one_char
    
    return cipher_text


def decipher(cipher_text, cipher_key):
    dechiper_text = ""

    for one_char in cipher_text:
        if one_char.isalpha():
            if one_char.isupper(): # 65-90
                ascii_value = ord(one_char) - cipher_key
                if ascii_value < 65:
                    ascii_value = ascii_value + 26 
            else: # 97-122
                ascii_value = ord(one_char) - cipher_key
                if ascii_value < 97:
                    ascii_value = ascii_value + 26 
            dechiper_text += chr(ascii_value)
        else:
            dechiper_text += one_char
    
    return dechiper_text


if __name__ == "__main__":
    main()


# # Another version:
# 
# def main():
#     plain_text = input("\nIngrese un mensaje: ")
#     cipher_key = int(input("Ingrese el desplazamiento: "))
#     cipher_text   = caesar(plain_text, cipher_key)
#     decipher_text = caesar(cipher_text, -cipher_key)
#     print(f"\nMensaje cifrado:    {cipher_text}")
#     print(f"Mensaje descifrado: {decipher_text}")
# 
# def caesar(text, key):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             base = 65 if char.isupper() else 97
#             result += chr((ord(char) - base + key) % 26 + base)
#         else:
#             result += char
#     return result
# 
# if __name__ == "__main__":
#     main()