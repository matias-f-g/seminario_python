"""Dado el siguiente texto almacenado en una variable, calcule e imprima:
    • La cantidad total de líneas.
    • La cantidad total de palabras.
    • El promedio de palabras por línea.
    • Todas las líneas cuya cantidad de palabras esté por encima del promedio.
"""


text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

total_lines = 0
total_words = 0

# Iterate over the lines
for line in text.splitlines():
    total_lines += 1
    total_words += len(line.split())

average_line = round(total_words / total_lines, 2)

print("\nTotal de líneas:", total_lines)
print("Total de palabras:", total_words)
print("Promedio de palabras por línea:", average_line)

print(f"\nLíneas por encima del promedio (es decir, que tienen más de {int(average_line)} palabras):")
for line in text.splitlines():
    n_words = len(line.split())
    if  n_words > int(average_line):
        print(f'- "{line}" ({n_words} palabras)')
