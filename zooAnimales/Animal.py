import gestion
class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", zona=None, zoo=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        self.zoo = zoo
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    def toString(self):
        if self.zona:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zoo.nombre}."
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}."

    @staticmethod
    def totalPorTipo():
        return (f"Mamíferos: {Animal.mamiferos}\nAves: {Animal.aves}\n"
                f"Reptiles: {Animal.reptiles}\nPeces: {Animal.peces}\nAnfibios: {Animal.anfibios}")
