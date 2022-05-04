import json
import vk_api
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from mod import films_duration, films_year, films_genre, random_img
TOKEN = 'fa08b59a045c6c6f861933963d3a2aadf7efbd01bf3292d7a08b7405afd2d3e658796555ea5f641b4e3e4'
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
vk = vk_api.VkApi(token=TOKEN)
vk.get_api()

keyboard = {
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
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "20"
                },
                "color": "primary"
            },
        ],
        [
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
                    "label": "23"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "24"
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

keyboard2 = {
    "one_time": True,
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
                    "label": "2001-2006"
                },
                "color": "primary"
            },
        ],  #
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2007-2015"
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

keyboard3 = {
    "one_time": True,
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
                    "label": "более 5 часов"
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
keyboard3 = json.dumps(keyboard3, ensure_ascii=False).encode('utf-8')
keyboard3 = str(keyboard3.decode('utf-8'))

longpoll = VkBotLongPoll(vk, 211179909)

genres = [str(i) for i in range(0, 25)]
years = {'1900-1950': '1', '1951-1970': '2', '1971-1980': '3', '1981-1990': '4',
         '1991-2000': '5', '2001-2006': '6', '2007-2015': '7', 'Не имеет значения': '0'}
durs = {'меньше часа': '1', '60-90 минут': '2', '91-150 минут': '3',
        '151-300 минут': '4', 'более 5 часов': '5', 'Не имеет значения': '0'}


def img(user_id, films):
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open(f'{random_img()}', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    vk.method("messages.send", {"peer_id": user_id, "message": f"{films}",
                                "attachment": f'photo{c["owner_id"]}_{c["id"]}', "random_id": random.randint(1, 2147483647)},)


def main():
    g = True
    y = False
    d = False
    while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            if g:
                vk.method("messages.send", {"peer_id": id, "message": "Какой жанр вы делаете посмотреть", 'keyboard': keyboard,
                                            "random_id": random.randint(1, 2147483647)},)
            g = False
            body = messages["items"][0]["last_message"]["text"]
            if body in genres and not g:
                genre = int(body)
                if films_genre(genre)[0]:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "А какой временой преиод?", 'keyboard': keyboard2,
                               "random_id": random.randint(1, 2147483647)},)
                    y = True
                else:
                    img(id, f"{films_genre(genre)[1]}")
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"Finish",
                               "random_id": random.randint(1, 2147483647)},)
                    break
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
                              {"peer_id": id, "message": f"Finish",
                               "random_id": random.randint(1, 2147483647)}, )
                    break
            elif body in durs.keys() and d:
                duration = int(durs[body])
                print(films_duration(genre, year, duration))
                img(id, f"{films_duration(genre, year, duration)}")
                vk.method("messages.send",
                            {"peer_id": id, "message": f"Finish",
                           "random_id": random.randint(1, 2147483647)}, )
                break
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "пожалуйста, укажите один из вариатов",   'keyboard': keyboard,
                           "random_id": random.randint(1, 2147483647)},)


if __name__ == '__main__':
    main()
