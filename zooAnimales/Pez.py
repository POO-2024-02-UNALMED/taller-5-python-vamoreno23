from .animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self):
        super().__init__()
        self.colorEscamas = None
        self.cantidadAletas = None
        Animal.peces += 1
        Pez.listado.append(self)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océanos", genero, "rosado", 2)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "mares", genero, "blanco", 3)
    
    @staticmethod
    def cantidadpeces():
        return len(Pez.listado)
