#-----------------------------Abstraction------------------------------#
from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Abstract):
    def __init__(self,side):
        self.sides = side

    def perimeter(self):
           print("created")
    def area(self):
           print("created")

class Circle(Abstract):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
       print("created")
    def area(self):
       print("created")

obj = Circle(4)
obj = Square(4)
