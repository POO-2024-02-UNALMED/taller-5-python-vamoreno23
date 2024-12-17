import sys
sys.path.append("C:\Users\vamor\OneDrive\Escritorio\POO\taller-5-python-vamoreno23")
from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona: Zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self) -> int:
        return sum(zona.cantidadAnimales() 
                   for zona in self._zonas)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas

    def setZona(self, zonas):
        self._zonas = zonas
