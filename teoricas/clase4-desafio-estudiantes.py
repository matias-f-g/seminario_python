"""Tenemos que procesar los datos de los estudiantes de las tres comisiones
de Python. Por cada estudiante contamos con su DNI, nombre, comisión,
puntos de teoría, puntos de práctica y ciudad de procedencia.
¿Qué opciones tenemos para almacenar estos datos en archivos de texto?
"""

students_data = [{'DNI': 12345, 'name': 'Guido Van Rossum', 'pts_teoria': 100, 'pts_practica': 50, 'city': 'Haarlem', 'group': 'info:TM'},
                {'DNI': 11111, 'name': 'Ada Lovelace', 'pts_teoria': 100, 'pts_practica': 50, 'city': 'Londres', 'group': 'info:TM'},
                {'DNI': 12345, 'name': 'Alan Turing', 'pts_teoria': 100, 'pts_practica': 50, 'city': 'Londres', 'group': 'info_TT'},
                {'DNI': 11111, 'name': 'Joan Clarke', 'pts_teoria': 100, 'pts_practica': 50, 'city': 'Londres', 'group': 'info_TT'}
                ]


# This would be a good way to have a file to process the data (basically in CSV format)

students_file = open("students_database.txt", "w")

categories = [str(key) for key in students_data[0].keys()]
header = ", ".join(cat for cat in categories) + "\n"
students_file.write(header)

for student in students_data:
    one_student = ", ".join(str(v) for v in student.values()) + "\n"
    students_file.write(one_student)


students_file.write("\n\n*********************************************\n\n")


# This would be a nice way to print the data

for index, student in enumerate(students_data):
    n_student = "\nStudent N° " + str(index+1) + "\n"
    students_file.write(n_student)
    for k, v in student.items():
        one_item = str(k) + ": " + str(v) + "\n"
        students_file.write(one_item)

students_file.close()

