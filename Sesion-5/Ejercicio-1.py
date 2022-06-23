import math


def area_triangulo(base, altura):
    # se halla el area del triangulo
    a = round((base * altura) / 2)
    return a


def area_circulo(r):
    # Se halla el area del un circulo
    ac = round(math.pi * (pow(r, 2)), 2)
    return ac

# se muestran las dos funciones
print("El área del triangulo es :", area_triangulo(20, 15))
print("El área del círculo es :", area_circulo(12))
