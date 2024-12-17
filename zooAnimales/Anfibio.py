class Anfibio(Animal):
    listado = []

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
        Animal.anfibios += 1

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)