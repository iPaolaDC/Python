# Creación del archivo de texto
file = open('archivo_de_texto.txt', 'w')
# Escribir en el archivo de texto
file.write("Esta es la primera linea del texto \n")
file.close()

# Escribir por segunda vez
file = open('archivo_de_texto.txt', 'r+')
file.readlines()
file.write("Esta es la segunda linea del texto \n")

