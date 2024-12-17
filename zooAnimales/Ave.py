class Ave(Animal):
    listado = []

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas=""):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)
        Animal.aves += 1

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        return cls(nombre, edad, "montañas", genero, "café glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        return cls(nombre, edad, "montañas", genero, "blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)