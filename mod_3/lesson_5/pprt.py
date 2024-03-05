a = {f"key{i}":"somedata" for i in range(15)}
from pprint import pprint
with open('data.txt','w') as f:
    pprint(a,f)