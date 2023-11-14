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
my_list.remove("SOME MORE TEXT!!!")
print(my_list)
# print(my_list[3])
# print(my_list)
# print(my_list[-4])
# for i in my_list:
#     print(i)
# # print("End of list")
print(len(my_list))