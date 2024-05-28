n = int(input())
price = {"E" : 10,
         "K" : 15,
         "B" : 30}
tax = {}
for i in range(n):
    mins, kat, name = input().split()
    if name in tax:
        tax[name] += int(mins) * price[kat]
    else:
        tax[name] = int(mins) * price[kat]
max_name = max(tax, key=tax.get)
print(max_name, tax[max_name])