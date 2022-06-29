def numero_primo():
    # Pedimos el número
    numero: int = int(input("Ingresa un número: "))
    while numero <= 1:
        numero: int = int(input("Los números primos son mayores que 1.Por favor ingresa nuevamente un número: "))

    for i in range(2, numero):
        # Evalua que el resto de la división sea igual a cero
        if (numero % i) == 0:
            print(numero, "NO es un número PRIMO")
            return False
    print(numero, "ES un número PRIMO")
    return True

numero_primo()
