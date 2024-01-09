from random import randint
from time import time
data = [str(randint(1,1_000_000)) for x in range(1_000_0000)]
start = time()
# max_str = max(data, key=lambda num: int(num))
print(str(max(map(int, data))))
# print((max_str))
print(time()-start)