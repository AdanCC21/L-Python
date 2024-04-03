"""
    Gonzalez Cesena Adan
    372799
    Gp941
    20/03/2024
"""

#ejercicio
calif={98,76,71,87,83,90,57,79,82,94}
sum=0
i=0
cont=0
for i in calif:
    sum+=i
    cont+=1

total=sum/cont
print(total)

#Ejercicio1--------------------------------------------------------------------------------------------------------
sum_calif = 0
cont = 0

print("Ingrese su calificación, -1 para salir")
calif = int(input())

while calif != -1:
    if calif == 0:
        print("No es posible dividir entre 0, por lo tanto no se agregará")
    else:
        sum_calif += calif
        cont += 1
    print("Ingrese su calificación, -1 para salir")
    calif = int(input())

if cont != 0:
    promedio = sum_calif / cont
    print("El promedio es:", promedio)
else:
    print("No se ingresaron calificaciones válidas.")
#Ejercicio2--------------------------------------------------------------------------------------------------------
"""
aprob=0
reprob=0

for i in range(10):
    print("Ingrese su resultado del examen")
    calif=int(input())

    if calif >=60:
        print("Aprobo")
        aprob+=1
    else:
        print("No aprobo")
        reprob+=1
print("total de aprobados",aprob,"total de reprobados",reprob)
"""
#Ejercicio3--------------------------------------------------------------------------------------------------------
"""
for i in range(2):
    print("ingrese un numero")
    num=int(input())
            
    if num%2==0:
        print("es par")
    else:
        print("es impar")
"""
#Ejercicio4--------------------------------------------------------------------------------------------------------
for i in range(99,-11,-11):
    print(i)

print("")

sum=0
for i in range(0,100,2):
    if i%2==0:
        sum+=i
    
print(sum)