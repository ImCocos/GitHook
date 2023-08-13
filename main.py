import asyncio
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from flask import Flask
from flask import request
import json
from threading import Thread, Event


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

        @dp.message_handler(lambda message: 1 == 2)
        async def start(message: types.Message):
            while True:

                cur_hours = time.localtime().tm_hour
                my_hours = hours[(cur_hours + 2) - (((cur_hours + 2) // 24) * 24)]
                if my_hours == 10 and self.flag1:
                    await bot.send_message(chat_id=-1001869856367, text=f'С добрым утром, ботяги, а также, работяги!\nПродуктивного дня <3\nНас пока что {await bot.get_chat_member_count(chat_id=-1001869856367)}')
                    self.flag1 = False
                    self.flag2 = True
                elif my_hours == 22 and self.flag2:
                    await bot.send_message(chat_id=-1001869856367, text=f'С добрым вечером, ботяги, а также, работяги!\nПриятных снов <3\nНас пока что {await bot.get_chat_member_count(chat_id=-1001869856367)}')
                    self.flag1 = True
                    self.flag2 = False

                if self.flag.is_set():
                    with open('COMMIT_INFO.json', 'rb') as f:
                        info = dict(json.loads(f.read()))
                    
                    hallo_part = random.choice(git_hallos)
                    commit_part = 'Коммиты:\n'
                    for commit in info['commits']:
                        commit_part += f'>Коммит от {commit["committer"]["name"]}:\n'
                        commit_part += f' -Дата:\n    {commit["timestamp"][:-6]}\n'
                        commit_part += f' -Сообщене:\n    {commit["message"]}\n'
                        commit_part += f' -Добавлено файлов: {len(commit["added"])}\n'
                        commit_part += f' -Изменено файлов: {len(commit["modified"])}\n'
                        commit_part += f' -Удалено файлов: {len(commit["removed"])}\n\n'
                    url = info['repository']['html_url']
                    
                    message_text = f'{hallo_part}\n\n'
                    message_text += commit_part
                    message_text += 'Пока всё, ботяги, а также работяги...\n\n'
                    message_text += f'Репозиторий - {url}'
                    
                    await bot.send_message(chat_id=-1001869856367, text=message_text)
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
