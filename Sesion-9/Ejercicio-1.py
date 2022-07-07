paises = input("Ingrese una lista de paises separados por comas: ")
paises_lista = set(paises.split(","))
print(", ".join(sorted(paises_lista)))
