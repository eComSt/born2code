def hello(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f'{i}:{j}')

hello('Jane','World',"PATREG BOG",message = "HELLLO",level = "warning")