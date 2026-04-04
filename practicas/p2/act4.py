"""Valide una dirección de email ingresada por el usuario con los siguientes criterios:
    1• Contiene exactamente un "@".
    2• Tiene al menos un carácter antes del "@".
    3• Tiene al menos un punto "." después del "@".
    4• No empieza ni termina con "@" ni con ".".
    5• La parte después del último punto tiene al menos 2 caracteres (el dominio).
"""

# Naturally, these rules do not apply in reality, and I tried to follow these
# (not the real ones, but the ones that appear in the exercise)

import re

# Some e-mails to test the regex fuction
emails = ["usuario@ejemplo.com",    # Valid
          "usuario@ejemplo..com",   # Valid
          "user@ejemplo.com.ar",    # Valid
          "%@.ue",                  # Valid
          "george@edu@info.com",    # Invalid (violates rule 1)
          "@ejemplo.com",           # Invalid (violates rule 2)
          "usuario@ejemplo",        # Invalid (violates rule 3)
          ".usuario@ejemplo.om",    # Invalid (violates rule 4)
          "usuario@ejemplo.w"       # Invalid (violates rule 5)
          ]

pattern = r"^[^@.][^@]*@[^@]*\.[^@.]{2,}$"

for email in emails:
    if re.match(pattern, email) is not None:
        print(f"El email {email} es válido") 
    else:
        print(f"El email {email} es inválido") 
