import sys
sys.path.append(r"C:\Users\vamor\OneDrive\Escritorio\POO\taller-5-python-vamoreno23")
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    # Métodos
    def agregarAnimales(self, animal: Animal):
        self._animales.append(animal)

    def cantidadAnimales(self) -> int:
        return len(self._animales)

    # Getters y Setters
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def notAnimales(self, animales):
        self._animales = animales
