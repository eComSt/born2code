def summ_digits(num):
    lst =[]
    for i in num:
        lst.append(int(i))
    return sum(lst)

ans = summ_digits(input())
print(ans)