import os
import asyncio
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from flask import Flask
from flask import request
import json
from threading import Thread, Event
import requests


api_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat=55.751244&lon=37.618423&appid=594156179360808d788f634d8738d7a8'

class Server:
    def __init__(self):
        self.flag = Event()

    def site(self):
        app = Flask(__name__)

        @app. route('/git-hook', methods=['POST'])
        def hook_root():
            json_dct = json.loads(request.data)
            dct = dict(json_dct)
            print(dct)

            with open('COMMIT_INFO.json', 'w') as f:
                json.dump(dct, f)
            
            if not self.flag.is_set():
                self.flag.set()
            
            return 'ok'

        app.run(host='0.0.0.0', debug=False)


    def bot(self):
        hours = [i for i in range(24)]


        git_hallos = ['Вы не поверите! Это же кто-то сделал обнову репозитория!!!',
              'Офигеть! Великий прогер всея Руси сделал очередную обнову репозитория...',
              'Вот это да, отвлекся от игр и сделал обнову репозитория!',
              'ЧТОООООО??!!? Обновил репо???!?',
            ]

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        bot = Bot(token='6672813444:AAHP28wMVnHWU32GoAaZ1LJS_WZbHc02EQY')
        dispatcher = Dispatcher(bot)
        self.flag1 = True
        self.flag2 = True
    
        print('##### Bot started running ##### ')
        bot = bot
        dp = dispatcher

        @dp.message_handler(commands=['test'])
        async def test(message: types.Message):
            pass

        @dp.message_handler(lambda message: 1 == 2)
        async def start(message: types.Message):
            while True:

                my_hours = time.localtime().tm_hour
                if my_hours == 10 and self.flag1:
                    weather_data = requests.get(api_weather_url).content
                    weather_data = json.loads(weather_data)

                    temp = round(float(weather_data['main']['temp']) - 273, 2)
                    pressure = weather_data['main']['pressure']
                    humidity = weather_data['main']['humidity']
                    max_temp = round(float(weather_data['main']['temp_max']) - 273, 2)
                    min_temp = round(float(weather_data['main']['temp_min']) - 273, 2)
                    wind_speed = round(float(weather_data['wind']['speed']), 2)

                    weather_text = f'Погода на сегодня:\n'
                    weather_text += f'  Температура: {temp}°С\n'
                    weather_text += f'  Температура(макс): {max_temp}°С\n'
                    weather_text += f'  Температура(мин): {min_temp}°С\n'
                    weather_text += f'  Давление: {pressure}мм рт.ст.\n'
                    weather_text += f'  Влажность: {humidity}\n'
                    weather_text += f'  Скорость ветра: {wind_speed}м/с\n'

                    await bot.send_photo(chat_id=-1001869856367, 
                                        photo=open(f'media/good_morning/{random.randint(8073, 8136)}.jpg', 'rb'), 
                                        caption=f'С добрым утром, ботяги, а также, работяги!\nПродуктивного дня <3\nНас пока что {await bot.get_chat_member_count(chat_id=-1001869856367)}\n{weather_text}')
                    self.flag1 = False
                    self.flag2 = True
                elif my_hours == 22 and self.flag2:
                    await bot.send_message(chat_id=-1001869856367, 
                                           text=f'С добрым вечером, ботяги, а также, работяги!\nПриятных снов <3\nНас пока что {await bot.get_chat_member_count(chat_id=-1001869856367)}')
                    self.flag1 = True
                    self.flag2 = False

                if self.flag.is_set():
                    with open('COMMIT_INFO.json', 'rb') as f:
                        info = dict(json.loads(f.read()))
                    
                    hallo_part = random.choice(git_hallos)
                    commit_part = 'Коммиты:\n'
                    for commit in info['commits']:
                        commit_part += f'Коммит от <a href="https://github.com/{commit["committer"]["name"]}">{commit["committer"]["name"]}</a>:\n'
                        commit_part += f' - Дата:\n        {commit["timestamp"][:-6]}\n'
                        commit_part += f' - Сообщение:\n        {commit["message"]}\n'
                        commit_part += f' - Добавлено файлов: {len(commit["added"])}\n'
                        commit_part += f' - Изменено файлов: {len(commit["modified"])}\n'
                        commit_part += f' - Удалено файлов: {len(commit["removed"])}\n\n'
                    url = info['repository']['html_url']
                    
                    message_text = f'{hallo_part}\n\n'
                    message_text += commit_part
                    message_text += 'Пока что всё, ботяги, а также работяги...\n\n'
                    message_text += f'Репозиторий - <a href="{url}">{info["repository"]["name"]}</a>'
                    
                    await bot.send_message(chat_id=-1001869856367, text=message_text, parse_mode='HTML')
                    self.flag.clear()
        
        executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start)
    
    def run(self):
        t1 = Thread(target=self.site)
        t2 = Thread(target=self.bot)

        t1.start()
        t2.start()
        t1.join()
        t2.join()


if __name__ == '__main__':
    s = Server()
    s.run()
