#пустые списки
# new_list = []
# text = ""
# text_list = list(text)
# print(new_list)

b = 42
my_list = [1, 2, 3,"TEXT",5,6,7,"SOME MORE TEXT!!!",b,b+17]
print(my_list)
my_list[3] = "NEW TEXT"
my_list.append("LAST ELEMENT")
my_list.insert(0,"FIRST ELEMENT")
my_list[0] = "NEW FIRST ELEMENT"
my_list.insert(4,"FOURTH ELEMENT")
print(my_list)
my_list.remove("SOME MORE TEXT!!!")
# del my_list[3]
# print(my_list)
# print(my_list[3])
# print(my_list)
# print(my_list[-4])
# for i in my_list:
#     print(i)
# # print("End of list")
# print(len(my_list))
# if 42 in my_list:
#     print("42 in list")
# else:
#     print("42 not in list")

list1 = [1, 2, 3,4]
list2 = [4, 5, 6, "NEXT"]
# print(list1 + list2)


# for i in my_list:
#     print(i)

# for i in range(len(my_list)):
#     print(i," элемент списка ",my_list[i])

x = [1,2,5,2,4,6,8,5,3]
# x.sort(reverse=True)
# y = sorted(x,reverse=True)

y = reversed(x)
print(x)
print(y)