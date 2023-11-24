#конкатенация
string = "Hello"
other_string = "World"
one_more_string = string + " " + other_string
# print(one_more_string)
#репликция
string = "Hello "
other_string = "!?"
one_more_string = string+other_string*10
# print(one_more_string)

#f строки
name = "Alex "
surname = "Frolov"
age = 25.25
gender = "male"
print(f"Hello, {name} {surname},{age} years old, {gender}!")
print("Hello, " + name +" "+ surname+ "," + str(age) + " years old, " + gender + "!")
for i in range(10):
    print(f'i = {i}')

#split
# string = "Hello, Alex Frolov, 25 years old, male!"
# lst = string.split()
# print(lst)
# new_lst = []
# for i in lst:
#     lst_1 = i.split(",")
#     for j in lst_1:
#         if len(j)!=0:
#             new_lst.append(j)
# print(new_lst)
string = "Hello, Alex Fro,lov, 25 years old, male!"
lst = string.split()
for i in range(len(lst)): #lst:
   lst[i]  = lst[i].replace(',','')
# print(lst)
# new_string = "".join(lst)
# print(string.count("lo"))
# upper = "руки вверх!"
# print(upper.upper())
# lower = "НЕ смей опускать руки!"
# print(lower.lower())
# capitalize = "сейчас в стране ПРОИСХОДИТ глобальная капитализация!"
# print(capitalize.capitalize())
# title = "а это просто титул ._."
# print(title.title())

# lower = "НЕ смей опускать руки!".lower()
# print(lower[::-1])
# string = input().lower().replace(" ","")
# if string ==string[::-1]:
#     print("YES its palindrome")
# else:
#     print("NO")
# string = input("Enter city: ").lower()
# if "новосибирск" in string:
#     print("YES")
# else:
#     print("NO")
# Итерирование по строкам и метод isdigit()
# for sym in 'year2023':
#     if sym.isdigit():
#         print(sym)
