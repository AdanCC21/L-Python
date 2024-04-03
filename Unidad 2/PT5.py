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
print("Ingrese una cantidad de tiempo en segundos:")
st = int(input())

hr = st // 3600
sr = st % 3600
m = sr // 60
s = sr % 60

print("Horas:", hr,"Minutos:", m,"Segundos:", s)
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
print("ingrese un numero para saber si es capicua")
num=int(input())
reverso = 0
num_original = num

while num > 0:
    digito = num % 10
    reverso = reverso * 10 + digito
    num //= 10

if reverso == num_original:
    print("Son iguales, es capicua")
else:
    print("No son iguales, es capicua")

#Ejercicio 37------------------------------------------------------------ 
print("Ingrese una palabra o frase para saber si es palindromo o no")
texto_usuario = input()

# Convertir el texto a minúsculas
texto = ''
for char in texto_usuario:
    if 'A' <= char <= 'Z':
        char = chr(ord(char) + 32) 
    texto += char

# Eliminar los caracteres especiales y espacios
texto_sin_especiales = ''
for char in texto:
    if 'a' <= char <= 'z' or '0' <= char <= '9':
        texto_sin_especiales += char

#invertir texto
texto_invertido = ''
for i in range(len(texto_sin_especiales) - 1, -1, -1):
    texto_invertido += texto_sin_especiales[i]

if texto_sin_especiales == texto_invertido:
    print("El texto ingresado es un palíndromo.")
else:
    print("El texto ingresado no es un palíndromo.")






