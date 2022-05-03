import json
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from mod import films_duration, films_year, films_genre
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
                    "label": "5"
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

keyboard2 = {"one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1900-"
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
                    "label": "5"
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
        ]
        ]}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


longpoll = VkBotLongPoll(vk, 211179909)

genres = [str(i) for i in range(0, 25)]

def main():
    g = True
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
                              {"peer_id": id, "message": "А какой временой преиод?", #'keyboard': keyboard,
                               "random_id": random.randint(1, 2147483647)}, )
                else:
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"{films_genre(genre)[1]}",
                               "random_id": random.randint(1, 2147483647)}, )
                    vk.method("messages.send",
                              {"peer_id": id, "message": f"Finish",
                               "random_id": random.randint(1, 2147483647)},)
                    break
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "пожалуйста, укажите один из вариатов",   'keyboard': keyboard,
                           "random_id": random.randint(1, 2147483647)}, )


if __name__ == '__main__':
    main()
