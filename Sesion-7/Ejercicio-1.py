import operaciones


def calculador():

    a = input("Ingresa el primer número:")
    b = input("ingresa el segundo número:")

    a = int(a)
    b = int(b)

    res_suma = operaciones.suma(a, b)
    res_resta = operaciones.resta(a, b)
    res_multiplicar = operaciones.multiplicar(a, b)
    res_dividir = operaciones.dividir(a, b)
    print("El resultado de", a, "+", b, "=", res_suma)
    print("El resultado de", a, "-", b, "=", res_resta)
    print("El resultado de", a, "x", b, "=", res_multiplicar)
    print("El resultado de", a, "/", b, "=", res_dividir)


if __name__ == '__main__':
    calculador()
