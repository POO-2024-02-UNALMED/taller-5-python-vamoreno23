class Pez(Animal):
    listado = []

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
        Animal.peces += 1

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        return cls(nombre, edad, "océano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        return cls(nombre, edad, "océano", genero, "gris", 6)

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)