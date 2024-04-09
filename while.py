longitud= int(input("Pon el numero par para la longitud horizontal "))
caracter =input("ingrese un caracter ")

cadena_triangulo=' '
numero_espacio=longitud//2
numero_caracter=1

contador = 0
mitad=longitud // 2

renglon_parte1=0
while renglon_parte1<longitud//2:
    columna=0
    numero_caracter_renglon = numero_espacio + numero_caracter
    while columna <numero_caracter_renglon:
        if columna<numero_espacio:
            cadena_triangulo=' '
        else:
            cadena_triangulo = cadena_triangulo + caracter
        columna = columna + 1
    numero_caracter=numero_caracter +2
    numero_espacio = numero_espacio - 1
    cadena_triangulo = cadena_triangulo + '\n'
    renglon_parte1 = renglon_parte1 + 1

renglon_parte2=0
while renglon_parte2 <longitud:
    cadena_triangulo= cadena_triangulo + caracter
    renglon_parte2 = renglon_parte2 + 1
cadena_triangulo = cadena_triangulo +'\n'
        
print(cadena_triangulo)