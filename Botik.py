import json
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import random
import time


hours = [i for i in range(24)]


git_hallos = ['Вы не поверите! Это же кто-то сделал обнову репозитория!!!',
              'Офигеть! Великий прогер всея Руси сделал очередную обнову репозитория...',
              'Вот это да, отвлекся от игр и сделал обнову репозитория!',
            ]

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class Botik:
    def __init__(self, api_token):
        self.bot = Bot(token=api_token)
        self.dispatcher = Dispatcher(self.bot)
        self.flag1 = True
        self.flag2 = True
    
    def run(self):
        print('##### Bot started running ##### ')
        bot = self.bot
        dp = self.dispatcher

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


                with open('SEND_GIT_INFO.txt', 'r') as f:
                    cgi = f.read()
                send = True if cgi == '1' else False
                if send:
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
                    with open('SEND_GIT_INFO.txt', 'w') as f:
                        f.write('0')
        
        executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start)
