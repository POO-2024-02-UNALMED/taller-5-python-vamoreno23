from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
