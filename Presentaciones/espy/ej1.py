import random

print("Cantidad de tiradas:")
num=int(input())

win = []
lose = []

for i in range(12):
    w=0
    l=0
    for i in range (num):
        c = random.randint(1, 2)
        if c==1:
            w+=1
        else:
            l+=1
    win.append(w)
    lose.append(l)
    



print("Ganadas\n", win)
print("Perdidas\n", lose)
