from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass
    @abs
    def eat(self, food):
        pass
class Dog(Animal):
    def __init__(self, name:str, breed:str, size:str):
        self.name = name
        self.breed = breed
        self.size = size
    def makeSound(self):
        print("aaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    def eat(self, food):
        print(f"{self.name} is eating {food}")