import requests
import json

dct = {
    'commit message': 'Big chages',
    'date': '09.08.2023',
    'files changed': '132324',
    'files deleted': '211',
}

json_dct = json.dumps(dct)

requests.post(url='http://127.0.0.1:5000/git-hook', data=json_dct)