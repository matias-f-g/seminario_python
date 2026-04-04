"""Eres ayudante en una cátedra que recibió registros de alumnos desde múltiples fuentes.
Los datos llegaron con errores: nombres con formatos inconsistentes, notas faltantes,
registros nulos y alumnos duplicados con distintas notas.
Tu tarea es limpiar los datos y generar un listado final.

Debe realizar las siguientes operaciones:
    • Eliminar registros con nombre nulo, vacío o solo espacios.
    • Eliminar registros con nota nula, vacía o no numérica (como "absent").
    • Normalizar nombres a formato título y estados a formato título.
    • Eliminar duplicados por nombre, quedándose con la nota más alta de cada alumno.
    • Ordenar alfabéticamente por nombre.
"""

students = [
            {"name": " Ana García ", "grade": "8", "status": "aprobado"},
            {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
            {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
            {"name": "ana garcía", "grade": "9", "status": "aprobado"},
            {"name": None, "grade": "7", "status": "aprobado"},
            {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
            {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
            {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
            {"name": " ", "grade": "5", "status": "aprobado"},
            {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
            {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
            {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
            {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
            {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
            {"name": "roberto díaz", "grade": "", "status": "Ausente"},
            {"name": None, "grade": None, "status": None},
            {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
            {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
            {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
            {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
            ]


# The new clean list
students_final = []

for student in students:
    # Check for correct name and grade
    if (student["name"] is None) or (student["name"].strip() == ""):
        continue
    if (student["grade"] is None) or (not student["grade"].isnumeric()):
        continue

    # Create a new clean student
    new_student = {"name": student["name"].strip().title(),
                   "grade": student["grade"].strip(),
                   "status": student["status"].strip().title()
                   }

    # Returns the index of a student in a list of students, or None if not present
    index = next((i for i, s in enumerate(students_final) if s["name"] == new_student["name"]), None)

    # If the student is not in the list, we add it; else, we preserve the best grade
    if index is None:
        students_final.append(new_student)
    elif int(new_student["grade"]) > int(students_final[index]["grade"]):
        students_final[index] = new_student
        

# Sort the list by name
students_final = sorted(students_final, key=lambda student:student["name"])

# Print the list in a nice way
print()
print(" Registro limpio de alumnos ".center(42, "-"))
print("Nombre".ljust(22), "Nota".ljust(6), "Estado")
print("-" * 42)

for student_f in students_final:
    print(student_f["name"].ljust(22), student_f["grade"].ljust(6), student_f["status"])

print("\nTotal de alumnos válidos:", len(students_final))