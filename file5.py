"""
    Gonzalez Ceseña Adan
    372799
    Grupo 941
    06/03/2024
"""

#Pre ejercicio--------------------------------------------
x=7
exp=1
while(x<=1000):
    x=7**exp
    exp=exp+1
#print(exp)

#ejercicio 1--------------------------------------------
print("")
c=1
while(c<=5):
    print(c)
    c=c+1

#ejercicio 2--------------------------------------------
print("")
c=5
while(c>0):
    print(c)
    c=c-1

#ejercicio 3--------------------------------------------
print("")
c=1
while(c<=5):
    print(c,end=' ')
    c=c+1

#ejercicio 4--------------------------------------------
print("")
c=5
while(c>0):
    print(c,end=' ')
    c=c-1

#ejercicio 5--------------------------------------------
print()
print("Ingrese un numero para hacer su sumatoria")
num=int(input())

c=0
sum=0
while(c<=num):
    sum=sum+c
    c=c+1
print("Su resultado es",sum)

#ejercicio 6--------------------------------------------
renglon=0
maximo_renglon=10
maximo_columna=16
cadena_renglon_columna=""

while renglon < maximo_renglon:
    columna=0
    while columna <maximo_columna:
        cadena_renglon_columna= cadena_renglon_columna + '♥' + ' '
        columna = columna +1
    cadena_renglon_columna=cadena_renglon_columna + '\n'
    renglon = renglon+1
print(cadena_renglon_columna)
