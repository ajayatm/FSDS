import abc
class Animal(abc.ABC):

    @abc.abstractmethod
    def getlegs(self):
        pass


class Mammal(Animal):
    def getlegs(self):
        pass

Tiger = Mammal()
print(Tiger.getlegs())