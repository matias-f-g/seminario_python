"""This program calculates how many Argentine films nominated for the Academy Award
for Best International Feature Film have a longer than average running time.
"""


def average_of_list(the_list):
    """Return the average of a list of numbers, or None if the list is empty."""
    if len(the_list) > 0:
        return (sum(the_list) / len(the_list))
    return None


def greater_than_average(the_list, average=None):
    """Return elements from the_list that exceed the average (calculated if not provided)."""
    if average is None:
        average = average_of_list(the_list)
    return [elem for elem in the_list if elem > average]


def main():
    movies_duration = [108, 105, 112, 115, 123, 129, 122, 140]
    avg = average_of_list(movies_duration)
    gta = greater_than_average(movies_duration, avg)
    print(f"Hay {len(gta)} película(s) que duran más que el promedio ({round(avg, 2)} min)")


if __name__ == "__main__":
    main()
