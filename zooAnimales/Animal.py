class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos : {Mamifero.caballos + Mamifero.leones}\n"
                f"Aves : {Ave.halcones + Ave.aguilas}\n"
                f"Reptiles : {Reptil.iguanas + Reptil.serpientes}\n"
                f"Peces : {Pez.salmones + Pez.bacalaos}\n"
                f"Anfibios : {Anfibio.ranas + Anfibio.salamandras}")
