# Se solicita el rango de numeros
numero_inicial: int = int(input('Ingresa un numero inicial: '))
numero_final: int = int(input('Ingresa un numero final: '))
# lista para guardar los numeros impares
numeros_impares: [int] = []

while numero_final <= numero_inicial:
    numero_final: int = int(input('El numero final debe ser mayor que el numero inicial. Ingresa nuevamente el numero final: '))
#recorer el rango de los numeros
for i in range(numero_inicial, numero_final+1):
    if i % 2 != 0:
        numeros_impares.append(i)
print(numeros_impares)