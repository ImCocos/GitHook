import json
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import random
import time


send_time = True

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
    
    def run(self):
        print('##### Bot started running ##### ')
        bot = self.bot
        dp = self.dispatcher

        @dp.message_handler(lambda message: 1 == 2)
        async def start(message: types.Message):
            while True:
                cur_hours = time.localtime().tm_hour
                if cur_hours == 12:
                    await bot.send_message(chat_id=-1001869856367, text=f'Сейчас {cur_hours} часов!')
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
