"""Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol.

El programa debe tener un menú interactivo con las siguientes opciones:
    1- Agregar un equipo al torneo.
    2- Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 - 2.
       El programa debe actualizar los puntos automáticamente (3 puntos por victoria,
       1 por empate, 0 por derrota).
    3- Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.
    4- Eliminar un equipo del torneo.
    6- Salir del programa.

Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un
resultado con un equipo desconocido, o ingresar un marcador con formato inválido.
"""

# Decidí agregar otra opción (la 5), que muestra el historial de los partidos,
# ya que se encontraban almacenados en una lista y resultaba muy fácil imprimirlos.

# Por otro lado, asumo que el nombre de los equipos es una sola palabra; para poder trabajar
# con nombres de más de una palabra, habría que modificar la función add_result().


MENU_TEXT = """
                MENÚ PRINCIPAL

1 --> para agregar uno o más equipos
2 --> para registrar uno más resultados
3 --> para ver la tabla de posiciones
4 --> para eliminar un equipo del torneo
5 --> para ver el historial de los resultados
6 --> para salir del programa

      Su opción: """


def main():
    print()
    print(' SIMULADOR DE TABLA DE POSICIONES PARA UN TORNEO DE FÚTBOL '.center(84, '*'))
    print('-' * 84)
    print('\nAviso: no se preocupe por las mayúsculas ni las minúsculas, pero sí por los espacios.\n\n')

    results = []
    table = {}

    while True:
        option = input(MENU_TEXT)
        
        # Ignore bad input
        if (option == '') or (not option.isnumeric()):
            continue
        else:
            option = int(option)
        
        print()
        match option:
            case 1: table = add_team(table)
            case 2: table, results = add_result(table, results)
            case 3: show_table(table)
            case 4: table = remove_team(table)
            case 5: show_history(results)
            case 6: break
            case _: print('Opción inválida')
        print()


def add_team(table):
    print(" AGREGAR EQUIPO(S) ".center(40, '-'))
    print("\nPara finalizar, ingrese 'listo'")

    team = input("Ingrese el nombre del equipo: ").capitalize()
    while team.lower() != "listo":
        # If (and only if) the team is not in the dictionary, it is added to the end of the table with 0 points
        table.setdefault(team, 0)
        team = input("Ingrese el nombre del equipo: ").capitalize()

    return table


def add_result(table, results):
    print(" AGREGAR ALGÚN RESULTADO ".center(70, '-'))
    print("\nIngrese cada resultado de la siguiente manera:")
    print("nombre_equipo_local nombre_equipo_visitante goles_local - goles_visitante")
    print("\nPor ejemplo, si quiere decir que boca le ganó a river 1 a 0 en la cancha de boca, escriba:")
    print("boca river 1 - 0")
    print("\nPreste atención a los espacios. Para finalizar ingrese 'listo'.")
    
    while True:
        print()
        game_result = input("Resultado: ")
        print()

        if (game_result == '') or (game_result.lower() == 'listo'):
            break
        
        game_result = game_result.strip().split()
        
        if len(game_result) != 5:
            print("La cantidad de elementos es incorrecta. Vuelva a intentar.")
            continue
        
        local_t, visitor_t, local_g, hyphen, visitor_g = game_result

        local_t = local_t.capitalize()
        visitor_t = visitor_t.capitalize()

        if (local_t not in table) or (visitor_t not in table):
            print("Alguno de los equipos no se encuentra en la tabla. Vuelva a intentar.")
            continue

        if (not local_g.isnumeric()) or (not visitor_g.isnumeric()):
            print("Alguno de los goles no se ingresó correctamente. Vuelva a intentar.")
            continue
        
        # Save the new result in the  list of results with a nice format
        results.append(f"{local_t} vs. {visitor_t}: {local_g} - {visitor_g}")

        # Increment score
        if local_g > visitor_g:
            table[local_t] += 3
        elif local_g < visitor_g:
            table[visitor_t] += 3
        else:
            table[local_t] += 1
            table[visitor_t] += 1

    # Returns the table sorted by scores in descending order and the updated results
    return dict(sorted(table.items(), key=lambda item: item[1], reverse=True)), results


def show_table(table):
    if len(table) > 0:
        print(" TABLA DE POSICIONES ".center(35, '-'))
        print('-' * 35)
        print("Equipos".ljust(25), "Puntos")
        print('-' * 35)
        for team_name, score in table.items():
            print(team_name.capitalize().ljust(25, '.'), score)
        print('-' * 35)
    else:
        print('La tabla está vacía')


def remove_team(table):
    team = input("\nIngrese el nombre del equipo que quiere eliminar: ").capitalize()
    if team in table:
        del table[team] 
    else:
        print(f"No se encontró a {team}")
    return table


def show_history(results):
    if len(results) > 0:
        print(" PARTIDOS REGISTRADOS ".center(30, '-'))
        for result in results:
            print(result)
    else:
        print('No hay ningún partido registrado')



if __name__ == "__main__":
    main()
