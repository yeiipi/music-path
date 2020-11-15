from pprint import pprint
import json
import glob
import os


fn = 'links'
# fn = 'nodes'

for filename in glob.glob('../relaciones/*.json'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        try:
            js = json.load(f)
            links = js[f'{fn}']
            pprint(filename)
            with open(f'./{fn}.json' , 'a+') as F:
                F.write(",\n".join(json.dumps(i) for i in links)+',\n')
        except json.decoder.JSONDecodeError:
            print(f'skip {filename}')



