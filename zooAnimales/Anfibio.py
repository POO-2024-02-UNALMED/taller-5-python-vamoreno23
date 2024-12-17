from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self):
        super().__init__()
        self.colorPiel = None
        self.venenoso = None
        Animal.anfibios += 1

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "charcos", genero, "verde", False)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "bosques", genero, "amarillo", True)
