reversor: int = 101
cuenta_regresiva: [int] = []

for i in range(1, reversor+1):
    rev = reversor-i
    cuenta_regresiva.append(rev)
print(cuenta_regresiva)