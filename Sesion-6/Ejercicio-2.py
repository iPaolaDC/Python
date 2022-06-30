class Alumno:

    # Iniciamos los atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def show_atributos(self):
        print("Alumno:", self.nombre)
        print("Nota:", self.nota)

        if self.nota >= 6:
            print("El alumno", self.nombre, ", Ha APROBADO la materia")
        else:
            print("El alumno", self.nombre, ", Ha NO APROBADO la materia")


alumno = Alumno("Paola", 9)
alumno.show_atributos()
