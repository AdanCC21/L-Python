import os
uni={}

def menu():
    os.system("clear")
    print("Menu")
    print("1.-Agregar estudiante")
    print("2.-Buscar estudiante por numero de identificacion")
    print("3.-Mostrar todos los estudiantes registrados")
    print("4.-Eliminar un estudiante")
    print("5.-Salir")
    print("Seleccione una opcion (1,2,3,4,5)")
    op = input()
    if op.isdigit():
        return int(op)
    else:
        return 0
    

op = 0
while op != 5:

    op = menu()
    
    if op == 1:
        print("Ingrese su identificador")
        Tid=input()
        print("Ingrese su nombre")
        Tname=input()
        uni[Tid]={Tname}
        print("El alumno",Tname,"Agregado correctamente")
    if op == 2:
        print("Ingrese el id del alumno a buscar")
        Tid=input()
        if Tid in uni:
            Tname=uni[Tid]
            print("Su nombre es",Tname)
        else:
            print("Usuario no existente")
    if op == 3:
        for ite, name in uni.items():
            print(ite,":",name)
    if op == 4:
        print("Ingrese el identificador del alumno que quiere eliminar")
        Tid=input()
        if Tid in uni:
            del uni[Tid]
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")
    if op == 5:
        print("Adioos")
    input()




