class Reptil(Animal):
    listado = []

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)
        Animal.reptiles += 1

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        return cls(nombre, edad, "jungla", genero, "blanco", 1)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)