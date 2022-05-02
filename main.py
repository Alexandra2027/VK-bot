import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from mod import films_duration, films_year, films_genre
TOKEN = 'fa08b59a045c6c6f861933963d3a2aadf7efbd01bf3292d7a08b7405afd2d3e658796555ea5f641b4e3e4'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 211179909)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Дорый день, какой жанр вы желаете посмореть? {films_duration(0, 2, 3)}",
                             keybord='',
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
