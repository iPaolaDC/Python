import pickle


# Crear la clase Vehiculo
class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return f'El vehiculo es de color {self.color} y tiene {self.puertas } puertas'

# Crear un objeto
objeto = Vehiculo("Rojo", "4")
print(objeto)

# Crear archivo
file = open('archivo_vehiculo', 'wb')

# Cargar en el archivo
pickle.dump(objeto, file)
file.close()
