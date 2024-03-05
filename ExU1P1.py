"""
    Gonzalez Cesenia Adan
    372799
    G 941
    Ejercicio 1
"""
print("Ingrese su primer numero")
n1=(int(input()))
print("Ingrese su segundo numero")
n2=(int(input()))
print("Ingrese su tercer numero")
n3=(int(input()))

cont = 0

#   Ifs
if n1 > n2:
    if n2 > n3:
        print("No son iguales")
        print("El orden de sus numeros es",n1,n2,n3)
        cont=1
    if n2==n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de sus numeros es",n1,n2,n3)
            cont=1
if n1 > n3:
    if n3 > n2:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n1,n3,n2)
            cont=1
    if n3 == n2:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n1,n3,n2)
            cont =1 
if n1==n2:
    if n3 >n2:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n3,n1,n2)
            cont =1
    if n3 < n2:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n1,n2,n3)
            cont=1
if n1==n3:
    if n2 >n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n2,n1,n3)
            cont=1
    if n2 < n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n1,n3,n2)
            cont =1

#n2-------------------------------------------
if n2 > n1:
    if n1 > n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de sus numeros es",n2,n1,n3)
            cont=1
    if n2 < n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de sus numeros es",n3,n2,n1)
            cont=1
    if n1 == n3:
        if cont ==0:
            print("No son iguales")
            print("El orden de sus numeros es",n2,n1,n3)
            cont =1
if n2 > n3:
    if n3 > n1:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n2,n3,n1)
            cont =1
    if n3 == n1:
        if cont ==0:
            print("El orden de tus numeros son",n2,n3,n1)
            cont =1

#n3-------------------------------------------
if n3 > n1:
    if n1 > n2:
        if cont ==0:
            print("No son iguales")
            print("El orden de sus numeros es",n3,n1,n2)
            cont =1
    if n1 == n2:
        if cont ==0:
            print("El orden de sus numeros es",n3,n2,n1)
            cont=1
    if n3 == n2:
        if cont ==0:
            print("El orden de sus numeros es",n3,n2,n1)
            cont =1
if n3 > n2:
    if n2 > n1:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n3,n2,n1)
            cont =1
    if n2 == n1:
        if cont ==0:
            print("No son iguales")
            print("El orden de tus numeros son",n3,n2,n1)
            cont =1



if n1 == n2:
    if n2 == n3:
        print("El orden de sus numeros son",n1,n2,n3)
        print("Todo los numeros son iguales")

