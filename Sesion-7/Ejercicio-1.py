import operaciones


def calculador():
    res_suma = operaciones.suma(10, 5)
    res_resta = operaciones.resta(10, 5)
    res_multiplicar = operaciones.multiplicar(10, 5)
    res_dividir = operaciones.dividir(10, 5)
    print("El resultado de la suma es:", res_suma)
    print("El resultado de la resta es:", res_resta)
    print("El resultado de la multiplicación es:", res_multiplicar)
    print("El resultado de la división es:", res_dividir)


if __name__ == '__main__':
    calculador()
