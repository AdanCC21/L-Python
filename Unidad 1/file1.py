#codigo_python_1.py
"""Comparar números enteros usando sentencias if y operadores de comparación."""

print('Ingrese dos números enteros y te diré', 'las relaciones que satisfacen.')

#lee el primer entero
numero1 = int(input('Ingrese el primer número entero: '))

#Lee el segundo entero
numero2 = int(input('Ingrese el segundo número entero: '))

if numero1 == numero2:
    print(numero1, 'es igual a', numero2)
    
if numero1 != numero2:
    print(numero1, 'no es igual a', numero2)
    
if numero1 < numero2:
    print(numero1, 'es menor que', numero2)
    
if numero1 > numero2:
    print(numero1, 'es mayor que', numero2)
    
if numero1 <= numero2:
    print(numero1, 'es menor o igual que', numero2)

if numero1 >= numero2:
    print(numero1, 'es mayor o igual que', numero2)


print("Comparacion\n")

c1 = 5<9
print(c1)
c2 = 5>9
print(c2)
c3 = 5>=9
print(c3)
c4 = 5 == 9
print(c4)
c5 = 5<=9
print(c5)
c6 = 9 !=5
print(c6)


