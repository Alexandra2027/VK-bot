import json
import vk_api
import requests
import random
from mod import films_duration, films_year, films_genre, random_img, add_film
from vk_api.bot_longpoll import VkBotLongPoll
TOKEN = 'fa08b59a045c6c6f861933963d3a2aadf7efbd01bf3292d7a08b7405afd2d3e658796555ea5f641b4e3e4'


vk = vk_api.VkApi(token=TOKEN)
vk.get_api()

# Клавиатура жанров поиска
keyboard = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "3"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "4"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "5"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "6"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "7"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "8"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "9"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "10"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "11"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "12"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "13"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "14"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "15"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "16"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "17"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "18"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "19"
                },
                "color": "primary"

            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "20"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "21"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "22"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "0"
                },
                "color": "primary"
            },
        ]

    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

# Клавиатура годов
keyboard2 = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1900-1950"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1951-1970"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1971-1980"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1981-1990"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1991-2000"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2001-2005"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2006-2010"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2011-2015"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2016-2022"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Не имеет значения"
                },
                "color": "primary"
            },
        ]
        ]
}
keyboard2 = json.dumps(keyboard2, ensure_ascii=False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))

# Клавиатура длительности
keyboard3 = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "меньше часа"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "60-90 минут"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "91-150 минут"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "151-300 минут"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Более 5 часов"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Меньше 5 часов"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Более 1.5 часов"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Меньше 2 часов"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Не имеет значения"
                },
                "color": "primary"
            },
        ]
    ]
}
keyboard3 = json.dumps(keyboard3, ensure_ascii=False).encode('utf-8')
keyboard3 = str(keyboard3.decode('utf-8'))

# Финальная клавиатура
finish_keyboard = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Показать другие фильмы"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Сделать новый запрос"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Добавить свой фильм"
                },
                "color": "positive"
            },
        ]

    ]
}
finish_keyboard = json.dumps(finish_keyboard, ensure_ascii=False).encode('utf-8')
finish_keyboard = str(finish_keyboard.decode('utf-8'))

# Стартовая клавиатура
start_keyboard = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Подобрать фильм"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Добавить свой фильм"
                },
                "color": "positive"
            },
        ]
    ]
}
start_keyboard = json.dumps(start_keyboard, ensure_ascii=False).encode('utf-8')
start_keyboard = str(start_keyboard.decode('utf-8'))

# Клавиатура жанров (добавление)
keyboard_g = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "3"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "4"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "5"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "6"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "7"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "8"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "9"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "10"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "11"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "12"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "13"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "14"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "15"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "16"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "17"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "18"
                },
                "color": "primary"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "19"
                },
                "color": "primary"

            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "20"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "21"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "22"
                },
                "color": "primary"
            },
        ]

    ]
}
keyboard_g = json.dumps(keyboard_g, ensure_ascii=False).encode('utf-8')
keyboard_g = str(keyboard_g.decode('utf-8'))

longpoll = VkBotLongPoll(vk, 211179909)

genres = [str(i) for i in range(0, 23)]
years = {'1900-1950': '1', '1951-1970': '2', '1971-1980': '3', '1981-1990': '4', '1991-2000': '5',
         '2001-2005': '6', '2006-2010': '7', '2011-2015': '8', '2016-2022': '9', 'Не имеет значения': '0'}
durs = {'меньше часа': '1', '60-90 минут': '2', '91-150 минут': '3',  '151-300 минут': '4',
        'Более 5 часов': '5', 'Меньше 2 часов': '6',  'Более 1.5 часов': '7', 'Меньше 5 часов': '8',
        'Не имеет значения': '0'}


# Функция отправки картинок
def img(user_id, films):
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open(f'{random_img()}', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    vk.method("messages.send", {"peer_id": user_id, "message": f"{films}",
                                "attachment": f'photo{c["owner_id"]}_{c["id"]}', "random_id": random.randint(1, 2147483647)},)


def main():
    g = False  # Флаг жанров 1
    y = False  # Флаг годов 1
    d = False  # Флаг длительности 1
    ag = False  # Флаг повтора
    plas = False  # Флаг добавления
    f = True  # Флаг начала
    name_f = False  # Флаг имени
    genr = False  # Флаг жанров 2
    date = False  # Флаг годов 2
    distans = False  # Флаг длительности 2
    dist = False  # Флаг добавления фильма
    while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if f:
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Что вы желаете сделать?", 'keyboard': start_keyboard,
                           "random_id": random.randint(1, 2147483647)}, )
                f = False
            elif body == 'Подобрать фильм':
                g = True
            elif body == 'Добавить свой фильм':
                plas = True
            if g:
                vk.method("messages.send", {"peer_id": id, "message": '''Какой жанр вы делаете посмотреть?
                Любой	0
                комедия	1
                драма	2
                мелодрама	3
                детектив	4
                документальный	5
                ужасы	6
                музыка	7
                фантастика	8
                анимация	9
                биография	10
                боевик	11
                приключения	12
                война	13
                семейный	14
                триллер	15
                фэнтези	16
                вестерн	17
                мистика	18
                короткометражный	19
                мюзикл	20
                исторический	21
                нуар	22''', 'keyboard': keyboard, "random_id": random.randint(1, 2147483647)},)
                g = False
            if body in genres and not g and not date and not distans:
                genre = int(body)
                if films_genre(genre)[0]:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "А какой временой преиод?", 'keyboard': keyboard2,
                               "random_id": random.randint(1, 2147483647)},)
                    y = True
                else:
                    img(id, f"{films_genre(genre)[1]}")
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                               "random_id": random.randint(1, 2147483647)}, )
                    ag = True
            elif body in years.keys() and y:
                year = int(years[body])
                if films_year(genre, year)[0]:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "длительность?", 'keyboard': keyboard3,
                               "random_id": random.randint(1, 2147483647)}, )
                    d = True
                    y = False
                else:
                    img(id, f"{films_year(genre, year)[1]}")
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                               "random_id": random.randint(1, 2147483647)}, )
                    ag = True
            elif body in durs.keys() and d:
                duration = int(durs[body])
                img(id, f"{films_duration(genre, year, duration)}")
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                           "random_id": random.randint(1, 2147483647)}, )
                ag = True
            elif ag:
                if body == 'Показать другие фильмы':
                    if not d and not y:
                        img(id, f"{films_genre(genre)[1]}")
                        vk.method("messages.send",
                                  {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                                   "random_id": random.randint(1, 2147483647)}, )
                    elif not d:
                        img(id, f"{films_year(genre, year)[1]}")
                        vk.method("messages.send",
                                  {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                                   "random_id": random.randint(1, 2147483647)}, )
                    elif not y:
                        img(id, f"{films_duration(genre, year, duration)}")
                        vk.method("messages.send",
                                  {"peer_id": id, "message": f"Приятного просморта", 'keyboard': finish_keyboard,
                                   "random_id": random.randint(1, 2147483647)}, )
                elif body == 'Добавить свой фильм':
                    plas = True
                    y = False
                    d = False
                    ag = False
                else:
                    g = True
                    y = False
                    d = False
                    ag = False
            elif plas:
                vk.method("messages.send", {"peer_id": id, "message": 'Введите название', "random_id": random.randint(1, 2147483647)},)
                name_f = True
                plas = False
            elif name_f:
                name = body
                name_f = False
                genr = True
            elif genr:
                vk.method("messages.send", {"peer_id": id, "message": '''Какой жанр у этого фильма?
                комедия	1
                драма	2
                мелодрама	3
                детектив	4
                документальный	5
                ужасы	6
                музыка	7
                фантастика	8
                анимация	9
                биография	10
                боевик	11
                приключения	12
                война	13
                семейный	14
                триллер	15
                фэнтези	16
                вестерн	17
                мистика	18
                короткометражный	19
                мюзикл	20
                исторический	21
                нуар	22''', 'keyboard': keyboard_g, "random_id": random.randint(1, 2147483647)},)
                date = True
                genr = False
            elif body in genres and date:
                gener = body
                vk.method("messages.send", {"peer_id": id, "message": 'Введите год выхода фильма', "random_id": random.randint(1, 2147483647)},)
                distans = True
                date = False
            elif body.isdigit() and int(body) >= 1900 and int(body) <= 2022 and distans:
                datic = int(body)
                vk.method("messages.send", {"peer_id": id, "message": 'Введите длительносить фильма (в минутах)', "random_id": random.randint(1, 2147483647)},)
                dist = True
            elif body.isdigit() and int(body) > 0 and dist:
                longs = int(body)
                add_film(name, gener, datic, longs)
                vk.method("messages.send",
                          {"peer_id": id, "message": "Ваш фильм успешно добавлен",
                           "random_id": random.randint(1, 2147483647)}, )
                g = False
                y = False
                d = False
                ag = False
                plas = False
                f = True
                name_f = False
                genr = False
                date = False
                distans = False
                dist = False


if __name__ == '__main__':
    main()
