""" Gonzalez Cesena Adan
    372799
    21/02/2024
"""

#Ejercicio 9
oB = ord('B')
oC= ord('C')
oD= ord('D')
ob=ord('b')
oc=ord('x')
od=ord('d')
oce=ord('0')
oca=ord('1')
oc2=ord('2')
ocs=ord('$')
ocac=ord('*')
ocdw=ord('+')
ocds=ord(' ')
print(oB, oC,oD,ob,oc,od,oce,oca,oc2,ocs,ocac,ocdw,ocds)

#Ejercicio 10
print("Ingrese su primer numero")
num1=int(input())

print("Ingrese su segundo numero")
num2=int(input())

print("Ingrese su tercer numero")
num3=int(input())

suma=num1+num2+num3
promedio=(suma)/3
producto=(num1*num2*num3)

#               Mayores
if num1 > num2:
    if num1 > num3:
        print("Tu numero mayor es",num1)

if num1 > num3:
    if num1 > num2:
        print("Tu numero mayor es",num1)

if num2 > num1:
    if num2 > num3:
        print("Tu numero mayor es",num2)
if num2 > num3:
    if num2 > num1:
        print("Tu numero mayor es",num2)

if num3 > num1:
    if num3 > num2:
        print("Tu numero mayor es",num3)
if num3 > num2:
    if num3 > num1:
        print("Tu numero mayor es",num3)

#               Menores

if num1 < num2:
    if num1 < num3:
        print("Tu numero menor es",num1)

if num1 < num3:
    if num1 < num2:
        print("Tu numero menor es",num1)

if num2 < num1:
    if num2 < num3:
        print("Tu numero menor es",num2)
if num2 < num3:
    if num2 < num1:
        print("Tu numero menor es",num2)

if num3 < num1:
    if num3 < num2:
        print("Tu numero menor es",num3)
if num3 < num2:
    if num3 < num1:
        print("Tu numero menor es",num3)

#Ejercicio 11 
print("ingrese su un numero de 5 digitos")
five=int(input())
if five > 10000:
    di1=five // 10000
    di2=(five // 1000)%10
    di3=(five // 100)%10
    di4=(five // 10)%10
    di5=five %10
    print(di1,di2,di3,di4,di5)

#   Ejercicio 12
p=100000
r=0.07
n1=10
n2=20
n3=30
a=p*(1+r)**n1
print("valor en 10 anios",a)
a=p*(1+r)**n2
print("valor en 20 anios",a)
a=p*(1+r)**n3
print("valor en 30 anios",a)

#Limite de caracteres
# import sys
# sys.set_int_max_str_digits(12300)

# x=60
# z=x**1000
# print(z)

#   Ejercicio 14
print("ingrese un numero")
last=int(input())
last=last%10
print("El ultimo digito de tu numero es",last)

#   Ejercicio 15
print("Ingrese su primer numero")
num1=float(input())

print("Ingrese su segundo numero")
num2=float(input())

print("Ingrese su tercer numero")
num3=float(input())

#               Menores

if num1 < num2:
    if num1 < num3:
        print("Tu numero menor es",num1)
        

if num1 < num3:
    if num1 < num2:
        print("Tu numero menor es",num1)

if num2 < num1:
    if num2 < num3:
        print("Tu numero menor es",num2)
if num2 < num3:
    if num2 < num1:
        print("Tu numero menor es",num2)

if num3 < num1:
    if num3 < num2:
        print("Tu numero menor es",num3)
if num3 < num2:
    if num3 < num1:
        print("Tu numero menor es",num3)

#   Ejercicio 17
print("Ingrese su primer numero")
num1=float(input())

print("Ingrese su segundo numero")
num2=float(input())

print("Ingrese su tercer numero")
num3=float(input())

#   Ifs
if num1 < num2:
    if num2 < num3:
        print("El orden de sus numeros es",num1,num2,num3)
if num1 < num3:
    if num3 < num2:
        print("El orden de tus numeros son",num1,num3,num2)

if num2 < num1:
    if num1 < num3:
        print("El orden de sus numeros es",num2,num1,num3)
if num2 < num3:
    if num3 < num1:
        print("El orden de tus numeros son",num2,num3,num1)

if num3 < num1:
    if num1 < num2:
        print("El orden de sus numeros es",num3,num1,num2)
if num3 < num2:
    if num2 < num1:
        print("El orden de tus numeros son",num3,num2,num1)


