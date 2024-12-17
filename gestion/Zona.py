class Zona:
    def __init__(self):
        self.nombre = ""  
        self.zoo = None  
        self.animales = []  

    def agregar_animales(self, animal):
        self.animales.append(animal)

    def cantidad_animales(self):
        return len(self.animales)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_zoo(self):
        return self.zoo

    def set_zoo(self, zoo):
        self.zoo = zoo

    def get_animales(self):
        return self.animales

    def set_animales(self, animales):
        self.animales = animales
