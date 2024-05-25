cadena = "El cuadrado del primer termino, mas el doble producto del primero por el segundo, mas el cuadrado segundo"
palabras = cadena.split(" ")

print("Palabra \t Contador")
print("------- \t --------")
for palabra in palabras:
    contador = palabras.count(palabra)
    print(f"{palabra:<16} {contador}")

print("\n\nPalabras unicas: ", len(set(palabras)))