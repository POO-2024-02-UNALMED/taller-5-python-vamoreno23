class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self):
        self.nombre = None
        self.edad = None
        self.habitat = None
        self.genero = None
        Animal.totalAnimales += 1

    def movimiento(self) -> str:
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos: {Animal.mamiferos}\n"
                f"Aves: {Animal.aves}\n"
                f"Reptiles: {Animal.reptiles}\n"
                f"Peces: {Animal.peces}\n"
                f"Anfibios: {Animal.anfibios}")

    def __str__(self):
        return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                f"habito en {self.habitat} y mi genero es {self.genero}")
