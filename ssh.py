import json
from pprint import pprint


with open('COMMIT_INFO.json', 'rb') as f:
    info = dict(json.loads(f.read()))
pprint(info)