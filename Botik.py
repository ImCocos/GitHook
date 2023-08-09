import json
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import random

git_hallos = ['Вы не поверите! Это же сам @ImCocos сделал коммит!!!',
              'Офигеть! Великий прогер всея Руси сделал очередной коммит...',
              'Вот это да, отвлекся от игр и сделал коммит!',
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
                with open('SEND_GIT_INFO.txt', 'r') as f:
                    cgi = f.read()
                send = True if cgi == '1' else False
                if send:
                    with open('COMMIT_INFO.json', 'rb') as f:
                        info = dict(json.loads(f.read()))
                    
                    message_text = random.choice(git_hallos) + '\n\n'
                    message_text += 'Коммит по прекраснейшему репозиторию:\n' + info['repository']['svn_url'] + '\n'
                    message_text += f'Коммит был совершен {info["repository"]["owner"]["login"]} в {info["repository"]["created_at"].replace("T", ";").replace("Z", "")}'
                    message_text += '.'
                    

                    await bot.send_message(chat_id=-1001869856367, text=message_text)
                    with open('SEND_GIT_INFO.txt', 'w') as f:
                        f.write('0')
        
        executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start)
