"""Dado el conjunto de datos de Spotify, queremos:

    1- Guardar en otro archivo, en formato json, las canciones que tienen
    asignado más de un género.

    2- Los cinco (5) artistas con más canciones en el dataset durante el año 2019.
"""

# Dataset downloaded from: https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019

# Prerequisite: I assume that all files are (and will be) in the current working directory.

import csv
import json
from collections import Counter


# Read all the data from the csv
with open('songs_normalize.csv', encoding='utf-8') as file_csv:
    csv_reader = csv.DictReader(file_csv)
    data = list(csv_reader)


# Select the songs with more than one genre
various_genres = list(filter(lambda song: len(song['genre'].split(',')) > 1, data))

# Write that new list of songs in the first json file
with open('j1_genres.json', 'w', encoding='utf-8') as file_json1:
    json.dump(various_genres, file_json1, indent=4)


# Filter the songs from 2019
songs_2019 = list(filter(lambda song: song['year'] == '2019', data))

# Count the number of appearances of the artists and select the first five
artists_counted = Counter(song['artist'] for song in songs_2019)
top5_artists = [artist for artist, count in artists_counted.most_common(5)]

# Write the top 5 in the second json file
with open('j2_top5_2019.json', 'w', encoding='utf-8') as file_json2:
    json.dump(top5_artists, file_json2, indent=4)
