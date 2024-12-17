class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    def toString(self):
        if self.zona and self.zona.getZoo():
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona.getNombre()}, en el {self.zona.getZoo().getNombre()}."
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}."

    @staticmethod
    def totalPorTipo():
        return f"Mamíferos: {len(Mamifero.listado)}\nAves: {len(Ave.listado)}\nReptiles: {len(Reptil.listado)}\nPeces: {len(Pez.listado)}\nAnfibios: {len(Anfibio.listado)}"