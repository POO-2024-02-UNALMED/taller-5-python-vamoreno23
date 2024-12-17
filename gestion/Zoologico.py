class Zoologico:
    def __init__(self):
        self._nombre = ""  
        self._ubicacion = ""  
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
        return total

    def getZona(self):
        return self._zonas

    def getNombre(self):
        return self._nombre
