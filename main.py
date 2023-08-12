from flask import Flask
from flask import request
from flask import json
from threading import Thread
from Botik import Botik
from AliveKeeper import AliveKeeper


def site():
    app = Flask(__name__)

    @app. route('/git-hook', methods=['POST'])
    def hook_root():
        json_dct = json.loads(request.data)
        dct = dict(json_dct)
        print(dct)

        with open('COMMIT_INFO.json', 'w') as f:
            json.dump(dct, f)
        
        with open('SEND_GIT_INFO.txt', 'w') as f:
            f.write('1')
        
        return 'ok'

    app.run(host='0.0.0.0', debug=False)


def bot():

    b = Botik(api_token='6672813444:AAHP28wMVnHWU32GoAaZ1LJS_WZbHc02EQY')
    b.run()


def keep_alive():
    ak= AliveKeeper(ping_url='https://githook.codimcocos.repl.co')
    ak.keep_alive()


if __name__ == '__main__':
    t1 = Thread(target=site)
    t2 = Thread(target=keep_alive)
    t3 = Thread(target=keep_alive)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
