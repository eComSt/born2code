from time import sleep

def pBB(n, i, t): 
    pb = ""
    for j in range(40):
        if j <= int(40*i//t):
            pb += "▮"
        else:
            pb+= "▯"
    perc = "{0:.1f}".format(100*i/t)
    return f'\r{n}\t[{pb}] {perc}% \t {i}/{t}'
    
for i in range(10):
    x = pBB("Progress",i+1,10)
    print(x, end="")

    