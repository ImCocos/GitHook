from flask import Flask
from flask import request
from flask import json
from threading import Thread
from Botik import Botik

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


if __name__ == '__main__':
    t = Thread(target=site)
    t.start()
    bot()
