""" 
    Gonzalez Cesena Adan
    372799
    28/02/2024
"""

#Ejercicio en clase----------------------------------------
calificacion = 85
calificacion == 85  
if(calificacion>=60):
    print("aprobado papu")
else:
    print("FUERA DE PAPULANDIA")

resultado = ('Aprobado' if calificacion>=60 else 'Reprobado')

print("Resultado",resultado)

#Ejercicio 1------------------------------------------------
print("ingrese un numero para comprobar si es par o impar")
num1=int(input())

if(num1%2 > 0):
    print("Su numero es impar")
else:
    print("Su numero es par")

print("ingrese un segundo para comprobar si es par o impar")
num2=int(input())

if(num2%2 > 0):
    print("Su numero es impar")
else:
    print("Su numero es par")

#Ejercicio 2------------------------------------------------
print("ingrese el primer numero entero")
num1=int(input())

print("ingrese el segundo numero entero")
num2=int(input())

if(num1>num2):
    if num1%num2 > 0:
        print(num2,"No es multiplo de",num1)
    else:
        print(num2,"Es multiplo de",num1)
else:
    if num2%num1 > 0:
        print(num1,"No es multiplo de",num2)
    else:
        print(num1,"Es multiplo de",num2)

#Ejercicio 3----------------------------------------------------------
print("Ingrese el primer numero")
num1=int(input())

print("Ingrese el segundo numero")
num2=int(input())

print("Ingrese el tercero numero")
num3=int(input())

if(num1==num2):
    if(num2==num3):
        print("son iguales")
else:
    print("No son iguales")
    
#Ejercicio 4---------------------------------------------------------
print("Ingrese su calificion")
calif=int(input())

if(calif>=90):
    print("A")
elif(calif>=80):
    print("B")
elif(calif>=70):
    print("C")
elif(calif>=60):
    print("D")
else:
    print("F")


