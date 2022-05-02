import sqlite3
import random

con = sqlite3.connect("films.sqlite")
cur = con.cursor()


def films_genre(genre):
    if genre != 0:
        result1 = cur.execute("""SELECT * FROM films
                   WHERE genre = ?""", (genre,)).fetchall()
        result = [result1[i][1] for i in range(len(result1))]
        print(result)
        if not bool(result1):
            return (False, 'Таких фильмов нет')
        elif len(result1) >= 3 and len(result1) < 20:
            film = random.sample(result1, 3)
            return (False, film)
        elif len(result1) >= 20:
            return (True, None)
        else:
            return (False, result1)
    else:
        return (True, None)


def films_year(genre, date):
    if genre != 0 and date != 0:
        years = cur.execute("""SELECT * FROM years
                WHERE id = ?""", (date,)).fetchone()
        year1 = years[1]
        year2 = years[2]
        result2 = cur.execute("""SELECT * FROM films
                          WHERE year >= ? AND year <= ? AND genre = ?""", (year1, year2, genre)).fetchall()
        result2 = [result2[j][1] for j in range(len(result2))]
        if not bool(result2):
            return (False, 'Таких фильмов нет')
        elif len(result2) >= 3 and len(result2) < 20:
            film = random.sample(result2, 3)
            return (False, film)
        elif len(result2) >= 20:
            return (True, None)
        else:
            return (False, result2)
    else:
        return (True, None)


def films_duration(genre, date, duration):
    if genre != 0:
        years = cur.execute("""SELECT * FROM years
                    WHERE id = ?""", (date,)).fetchone()
        year1 = years[1]
        year2 = years[2]
        durations = cur.execute("""SELECT * FROM duration
                    WHERE id = ?""", (duration,)).fetchone()
        duration1 = durations[1]
        duration2 = durations[2]
        result2 = cur.execute("""SELECT * FROM films
                          WHERE year >= ? AND year <= ? AND genre = ? AND duration >= ? AND duration <= ?""",
                              (year1, year2, genre, duration1, duration2)).fetchall()
        result2 = [result2[j][1] for j in range(len(result2))]
        if not bool(result2):
            return 'Таких фильмов нет'
        elif len(result2) >= 3:
            film = random.sample(result2, 3)
            return film
        else:
            return result2
    else:
        years = cur.execute("""SELECT * FROM years
                    WHERE id = ?""", (date,)).fetchone()
        year1 = years[1]
        year2 = years[2]
        durations = cur.execute("""SELECT * FROM duration
                    WHERE id = ?""", (duration,)).fetchone()
        duration1 = durations[1]
        duration2 = durations[2]
        result2 = cur.execute("""SELECT * FROM films
                          WHERE year >= ? AND year <= ? AND duration >= ? AND duration <= ?""",
                              (year1, year2, duration1, duration2)).fetchall()
        result2 = [result2[j][1] for j in range(len(result2))]
        if not bool(result2):
            return 'Таких фильмов нет'
        elif len(result2) >= 3:
            film = random.sample(result2, 3)
            return film
        else:
            return result2
