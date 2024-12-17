from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre="", edad=0, habitat="", genero="", pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return cls(nombre, edad, "pradera", genero, pelaje=True, patas=4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return cls(nombre, edad, "selva", genero, pelaje=True, patas=4)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)