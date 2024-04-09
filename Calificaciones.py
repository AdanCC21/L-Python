suma=0
prom=0
count=0
calif=0
ap=0
rp=0

while calif > -1:
    print("ingrese la calificacion, -1 para terminar")
    calif=int(input())

    if calif>100 or 0:
        print("“La calificación está fuera del rango establecido, por favor ingrese una calificación entre 0 y 100")
        
    else:
        if calif != -1:
            count+=1
            suma=suma+calif
            if calif>=60:
                ap+=1
            if calif>=0 and calif <60:
                rp+=1


print("")

if suma==0:
    print("No se ingresaron calificaciones")
else:
    prom=suma//count
    
    print("prmedio de las calificaciones capturadas del segundo exmane parcial :",prom)
    print("Cantidad de alumnos aprobados en el examen segundo parcial",ap)
    print("Cantidad de alumnos reprobados en el examen segundo parcial",rp)
    if prom >= 90:
        print("El docente obtuvo buen desempeño en el segundo parcial.")
    else:
        print("El docente no obtuvo buen desempeño en el segundo parcial.")
        




