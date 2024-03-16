"""
    Adan Gonzalez Ceseña
    Gp 941
    15/03/2024
    Practica 5
"""

#Ejercicio 30------------------------------------------------------------
cad1="Horas"
cad2="Numero de bacterias"
bact=200
time=0
bactN=0

print(cad1,"\t",cad2, sep=(""))
for i in range(5):
    print(time,"\t",bactN,sep=(""))
    time+=5
    bactN=200*2**time

print("")
time=0
bactN=0
for i in range(5):
    print(f"{cad1:>5} {cad2:>25}")
    print(f"{time:>0} {bactN:>28}")
    time+=5
    bactN=200*2**time


#Ejercicio 31------------------------------------------------------------
print("Ingrese una cantidad de tiempo en segundos")
time=int(input())


h = time // 3600
time = time % 3600 
m = time // 60
s = time % 60

print(h,m,s, sep=("-"))

#Ejercicio 32------------------------------------------------------------
"""
print("Ingrese una cantidad de tiempo en segundos")
time=int(input())


h = time // 3600
time = time % 3600 
m = time // 60
s = time % 60

print(h,m,s, sep=("-"))
"""
#Ejercicio 33------------------------------------------------------------
print("Ingrese un numero")
num=int(input())
suma=0

for i in range(1,num):
    if num%i==0:
        suma=suma+i

print("el numero",num,"",end=(""))
if suma==num:
    print("es perfecto")
else:
    print("imperfecto")

#Ejercicio 34------------------------------------------------------------
print("ingrese un numero binario")
binario=int(input())
pb=binario

decimal = 0
posicion = 0
while binario > 0:
    digito = binario % 10
    decimal += digito * (2 ** posicion)
    binario //= 10
    posicion += 1

print("el numero",pb,"Es equivalente a", decimal)

#Ejercicio 35------------------------------------------------------------
print("ingrese un numero binario")
decimal=int(input())
dc=decimal
binario = 0
posicion = 1
while decimal > 0:
    digito_binario = decimal % 2
    binario += digito_binario * posicion
    decimal //= 2
    posicion *= 10

print("el numero",dc,"Es equivalente a", binario)
#Ejercicio 36------------------------------------------------------------ 


#Ejercicio 37------------------------------------------------------------ 
print("Ingrese una frase")
cad=input()



