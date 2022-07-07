from functools import reduce

# Defino la lista
lista = []

# Solicito la cantidad de elementos que el usuario quiere en la lista
rango = int(input("Ingrese la cantidad de valores de la lista\n"))

# solicitar los valores de la lista
for x in range(rango):
    numeros = int(input("Ingrese un número:\n"))
    lista.append(numeros)

# filtramos los numeros pares
impares = filter(lambda a: a % 2, lista)

# hacemos la suma
impares = list(impares)
suma = reduce(lambda a, b: a + b, impares)

# imprimimos el valor
print("la lista de los numero impares es: ", impares)
print("la suma de todos los impares es : ", suma)
