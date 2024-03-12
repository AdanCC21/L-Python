"""
    Adan Gonzalez Ceseña
    Gp 941
    12/03/2024
"""
"""
#For iterador in iterable
for c in "hola":
    print(c,end=" ")
#sep
print(10,20,30, sep=",")

#{}
print(f'{10+5}+{20}+{30}',90,sep=", ")

#listas aunque no las vamos a usar
total=0
for numero in [2,-3,0,17,9]:
    total=total+numero
print(total)

#Range
for contador in range(10):
    print(contador, end=" ")
print("")
"""

#EJERCICIOS--------------------------------------------------------------------------
#1----------------
total=0
for c in range(100):
    total=total+(c+1)
print(total)

#2 26----------------------------------------------------------------------------
print("ejercio 26")
c=1
for co in range(5):
    print(c)
    c=c+1

print("")
for c in [1,2,3,4,5]:
    print(c)

print("")
for c in "12345":
    print(c,sep="")
print("")

#3 27----------------------------------------------------------------------------
print("ejercio 27")
c=5
for co in range(5):
    print(c)
    c=c-1

print("")
for c in [5,4,3,2,1]:
    print(c)

print("")
for c in "54321":
    print(c,sep="")
print("")


#4 28---------------------------------------------------------------------------
print("ejercio 28")
c=1
for co in range(5):
    if co<4:
        print(c,",",sep="",end="")
    else:
        print(c,end="")
    c=c+1

print("")
for c in [1,2,3,4,5]:
    if c<5:
        print(c,",",sep="",end="")
    else:
        print(c,end="")

print("")#------------------
co=0
for c in "12345":
    co=co+1
    if co<5:
        print(c,",",sep="",end="")
    else:
        print(c,end="")

print("")
#4 29-----------------------------------------------------------
print("ejercio 29")
c=5
for co in range(5):
    if co<4:
        print(c,",",sep="",end="")
    else:
        print(c,end="")
    c=c-1

print("")
for c in [5,4,3,2,1]:
    if c>1:
        print(c,",",sep="",end="")
    else:
        print(c,end="")

print("")#-----------------------------------------------------------------------------
co=0
for c in "54321":
    co=co+1
    if co<5:
        print(c,",",sep="",end="")
    else:
        print(c,end="")
