from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self):
        super().__init__()
        self.pelaje = None
        self.patas = None
        Animal.mamiferos += 1

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "selvas", genero, "verde", 5)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "desiertos", genero, "marron", 3)
