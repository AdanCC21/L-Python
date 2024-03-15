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


