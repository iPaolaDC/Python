class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "color:{}, Ruedas:{}, puertas:{}".format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color:{}, Ruedas:{}, puertas:{}, Km/h:{}, CC:{}".format(self.color, self.ruedas, self.puertas,
                                                                        self.velocidad, self.cilindrada)


objeto = Coche("verde", 4, 5, 60, 200)
print(objeto)
