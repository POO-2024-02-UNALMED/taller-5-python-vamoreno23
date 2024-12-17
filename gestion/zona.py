from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre=None, zoologico=None):
        self.nombre = nombre
        self.zoo = zoologico 
        self.animales = []

    def agregarAnimales(self, animal: Animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)





    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getZoo(self):
        return self.__zoologico

    def setZoo(self, zoo):
        self.__zoologico = zoo
