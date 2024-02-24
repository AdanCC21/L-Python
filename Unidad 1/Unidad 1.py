""" Gonzalez Ceseña Adan 
    372799
    Ejercicios Unidad I    
"""

import math

#Ejercicio 1
x=2
y=3

print('x= ',x)
print('valvue of',x,'is',(x+x))
print('x=')
print((x+y),'x=',(y+x))

#Calificacion prueba de if
calificaion = int(input('Ingrese una calificacion entre el 1 y el 100\n'))

if calificaion >= 90:
    print("felicidades tu calificacion 91 te otorga un A en este curso")
if calificaion < 90:
    print("Calificacion normal")

#Caluclar el diametro de un circulo
print("valores de ciruclos\n")
r=2
pip=3.14159

dia= 2 * r
circ=2 * pip * r
area=pip * r ** 2

print("diametro=",dia,"circunferencia=",circ,"Area=",area,'\n')

#Numero par o impar
print("ingrese un numero para determinar si es par o impar")
num=int(input())
if num%2 == 0:
    print("Es numero par")
if num%2 !=0:
    print("Es numero impar")

#multiplos
print("ingrese el primer numero entero")
num1=int(input())

print("ingrese el segundo numero entero")
num2=int(input())

if num2%num1 != 0:
    print(num2,"No es multiplo de",num1)

if num2%num1 == 0:
    print(num2,"Es multiplo de",num1)

#Tabla de cuadrados
print('numero','\t','cuadrado','\t','cubo')
print(0,'\t',0,'\t',0)
print(1,'\t',1,'\t',1)
print(2,'\t',4,'\t',8)
print(3,'\t',9,'\t',27)
print(4,'\t',16,'\t',64)
print(5,'\t',25,'\t',125)

#Alinear a la derecha
print('numero','\t','cuadrado','\t','cubo')
print(f"{0:>5}\t{0:>8}\t{0:>5}")
print(f"{1:>5}\t{1:>8}\t{1:>5}")
print(f"{2:>5}\t{4:>8}\t{8:>5}")
print(f"{3:>5}\t{9:>8}\t{27:>5}")
print(f"{4:>5}\t{16:>8}\t{64:>5}")
print(f"{5:>5}\t{25:>8}\t{125:>5}")



