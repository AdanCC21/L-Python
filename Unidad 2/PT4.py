"""
    Gonzalez Ceseña Adan
    372799
    Grupo 941
    06/03/2024
    Practica 4
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

#ejercicio 7--------------------------------------------
print("Ingrese su nombre")
cad=input()
print("Ingrese el simobolo que rodeara su nombre")
sim=input()

cadlen=len(cad)
c=0
top=""
center=""
while(c<=cadlen +1):
    top=top + sim
    c=c+1
print(top)
center = sim + cad + sim
print(center)
print(top)

#ejercicio 8--------------------------------------------
print("Ingrese un numero impar para iniciar su piramide")
nimpar=int(input())
caracter="*"
if nimpar % 2 == 0:
    print("El número no es impar")
else:
    n = 1
    espacios = nimpar // 2
    while n <= nimpar:
        print(" " * espacios + caracter * n)
        n += 2
        espacios -= 1
    
    n -= 4
    espacios = 1
    while n > 0:
        print(" " * espacios + caracter * n)
        n -= 2
        espacios += 1
