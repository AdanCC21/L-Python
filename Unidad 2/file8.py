"""
    Clase 03/04/2024
    Gonzalez Ceseña Adan
    372799
    Gp 941
"""

from decimal import Decimal

capital=1000
interes=0.05

for i in range(1,11):
    a=capital * (1+interes) ** i
    print(f'{i:>2}{a:>10.2f}')





