import random 
rannum_1 = random.sample ( range(1,100),int(input()))
rannum_2 = random.sample (range(1,100),int(input()))
my_set=set(rannum_1)
my_set_2=set(rannum_2)
print(len(my_set.intersection(my_set_2)))
