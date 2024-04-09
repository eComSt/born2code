with open('hero.txt') as f:
    data = f.read()

# f = open('hero.txt')
# data = f.read()
# f.close()
    
data_lower = data.lower()
lst= data_lower.split()
lst_stripped = [i.strip('. ",.!?/\\-+:"') for i in lst]
dct = {}
set_words = set(lst_stripped)
for i in set_words:
    c = lst_stripped.count(i)
    if c>100:
        dct[i] = c 
print(len(dct))
from pprint import pprint
pprint(dct)
# with open('data.csv','w') as f:
#     for word, count in dct.items():
#         f.write(f"{word} {count}\n")


