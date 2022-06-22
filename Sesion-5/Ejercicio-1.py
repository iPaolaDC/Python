import math


def area_triangulo(base, altura):
    a = round((base * altura) / 2)
    return a


def area_circulo(r):
    ac = round(math.pi * (pow(r, 2)), 2)
    return ac


print("El área del triangulo es :", area_triangulo(20, 15))
print("El área del círculo es :", area_circulo(12))
