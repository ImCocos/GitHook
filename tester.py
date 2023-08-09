import json
import pprint


dct = dict(json.loads(open('smth.json', 'rb').read()))

pprint.pprint(dct)
