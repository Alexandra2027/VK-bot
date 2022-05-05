import sqlite3
import random

con = sqlite3.connect("films.sqlite")
cur = con.cursor()


# Функция поска по жанрам
def films_genre(genres):
    genre = cur.execute("""SELECT * FROM genres
                   WHERE num = ?""", (genres,)).fetchone()[0]
    if genre != 0:
        result1 = cur.execute("""SELECT * FROM films
                   WHERE genre = ?""", (genre,)).fetchall()
        result = [str(result1[i][1]) + ' ' + str(result1[i][2]) for i in range(len(result1))]
        if not bool(result1):
            return (False, 'Таких фильмов нет')
        elif len(result) >= 3 and len(result) < 20:
            film = random.sample(result, 3)
            a = ''
            for j in range(len(film)):
                a += film[j] + '\n'
            return (False, a)
        elif len(result1) >= 20:
            return (True, None)
        else:
            a = ''
            for j in range(len(result)):
                a += result[j] + '\n'
            return (False, a)
    else:
        return (True, None)


# Функция поска по жанрам и по году издания
def films_year(genres, date):
    genre = cur.execute("""SELECT * FROM genres
                   WHERE num = ?""", (genres,)).fetchone()[0]
    if genre != 0 and date != 0:
        years = cur.execute("""SELECT * FROM years
                WHERE id = ?""", (date,)).fetchone()
        year1 = years[1]
        year2 = years[2]
        result2 = cur.execute("""SELECT * FROM films
                          WHERE year >= ? AND year <= ? AND genre = ?""", (year1, year2, genre)).fetchall()
        result2 = [str(result2[i][1]) + ' ' + str(result2[i][2]) for i in range(len(result2))]
        if not bool(result2):
            return (False, 'Таких фильмов нет')
        elif len(result2) >= 3 and len(result2) < 20:
            film = random.sample(result2, 3)
            a = ''
            for j in range(len(film)):
                a += film[j] + '\n'
            return (False, a)
        elif len(result2) >= 20:
            return (True, None)
        else:
            a = ''
            for j in range(len(result2)):
                a += result2[j] + '\n'
            return (False, a)
    else:
        return (True, None)


# Функция поска по жанрам, по году издания, длительности
def films_duration(genres, date, duration):
    genre = cur.execute("""SELECT * FROM genres
                   WHERE num = ?""", (genres,)).fetchone()[0]
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
        result2 = [str(result2[i][1]) + ' ' + str(result2[i][2]) for i in range(len(result2))]
        if not bool(result2):
            return 'Таких фильмов нет'
        elif len(result2) >= 3:
            film = random.sample(result2, 3)
            a = ''
            for j in range(len(film)):
                a += film[j] + '\n'
            return a
        else:
            a = ''
            for j in range(len(result2)):
                a += result2[j] + '\n'
            return a
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
        result2 = [str(result2[i][1]) + ' ' + str(result2[i][2]) for i in range(len(result2))]
        if not bool(result2):
            return 'Таких фильмов нет'
        elif len(result2) >= 3:
            film = random.sample(result2, 3)
            a = ''
            for j in range(len(film)):
                a += film[j] + '\n'
            return a
        else:
            a = ''
            for j in range(len(result2)):
                a += result2[j] + '\n'
            return a


# Функция выбота рандомной картинки
def random_img():
    n = random.choice([i for i in range(1, 15 + 1)])
    f = f'./img/{n}.jpg'
    return f


# Функция добавления фильма в дазу данных
def add_film(name, genres, date, duration):
    genre = cur.execute("""SELECT * FROM genres
                   WHERE num = ?""", (genres,)).fetchone()[0]
    cur.execute('''INSERT INTO films(title, genre, year, duration) VALUES (?, ?, ?, ?)''', (name, genre, date, duration))
    con.commit()
