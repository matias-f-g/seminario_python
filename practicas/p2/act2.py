"""Calcule la duración total de la playlist en formato Xm Ys,
y encuentre la canción más larga y la más corta.
"""

# Asumo que la playlist no está vacía y dura menos de una hora;
# si durara más de una hora, quizás convendría usar el módulo datetime

def main():

    playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]

    # Total time of the playlist in seconds
    playlist_seconds = 0

    # Max and min variables have the extra item "in_seconds" in order to compare easily and faster
    max_song = {"title": "...", "duration": "...", "in_seconds" : 0}
    min_song = {"title": "...", "duration": "...", "in_seconds" : 999999}

    for song in playlist:
        # First we get the total seconds from the song
        song_minutes, song_seconds = song["duration"].split(':')
        total_song_seconds = int(song_minutes)*60 + int(song_seconds)
        # Next, we add it to the total time and update the maximum and then the minimum
        playlist_seconds += total_song_seconds
        max_song, min_song = update_maxmin(song, total_song_seconds, max_song, min_song)

    total_minutes = playlist_seconds // 60
    total_seconds = playlist_seconds % 60

    print(f"Duración total: {total_minutes}m {total_seconds}s")
    print(f"Canción más larga: {max_song["title"]} ({max_song["duration"]})")
    print(f"Canción más corta: {min_song["title"]} ({min_song["duration"]})")


def update_maxmin(song, total_song_seconds, max_song, min_song):
    if total_song_seconds > max_song["in_seconds"]:
        song["in_seconds"] = total_song_seconds
        max_song = song
    if total_song_seconds < min_song["in_seconds"]:
        song["in_seconds"] = total_song_seconds
        min_song = song
    return max_song, min_song


if __name__ == "__main__":
    main()