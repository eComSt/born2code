import json
from pprint import pprint
# dct = {'name':  "Andrew", "age":26, 'isFullTime':True,"prog":["python","C","Assembler"]}
# with open("example.json",'w') as f:
#     json.dump(dct, f,indent = 4)

with open("example.json") as f:
    dct = json.load(f)

# pprint(dct)
if dct.get("isFullTime") and len(dct.get("prog")) > 1:
    print('Проходит на 1 этап')
else:
    print('Не проходит на 1 этап')
