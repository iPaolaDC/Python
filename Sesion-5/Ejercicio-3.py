def year_bisiesto():
    # pide el ingreso del año
    year: int = int(input("Ingresa el año: "))
    # validamos que los números sean mayores que 1
    while year <= 1:
        year: int = int(input("El año no es valido. Vuelve a ingresar el año"))

    # Para que sea bisiesto el año debe cumplir con esta condiciòn
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, "es un AÑO BISIESTO.(Tiene 366 días) ")
    else:
        print(year, "NO es un AÑO BISIESTO.(Tiene 365 días)")

year_bisiesto()
