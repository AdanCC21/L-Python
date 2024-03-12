"""
    Gonzalez Cesenia Adan
    372799
    G 941
    Ejercicio 2 cartera de huevos
"""

print("Ingrese la cantidad de huevos que obtuvo")
wb=int(input())

cl=wb//6
res=wb%6
res2=-1*(res-6)

if wb == 0:
    print("se llenaron",cl,"carteras de 6 huevos")
if wb < 6:
    if wb >1:
        print("se llenaron",cl,"carteras de 6 huevos")
        print("la ultima cartera tiene",res,"huevos")
        print("Faltan",res2,"Huevos para llenarla")
if wb == 6:
    print("La cartera se lleno con",wb,"huevos")

if wb > 6:
    print("se llenaron",cl,"carteras de 6 huevos")
    print("la ultima cartera tiene",res,"huevos")
    print("Faltan",res2,"Huevos para llenarla")