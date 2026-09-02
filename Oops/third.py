
#----------------------------inheritance-------------------------------#
#01.
# class FactoryMumbai:   #parent class/ super class
#     a= "i am an attribute memtioned inside in factory"
#     def hello(self):
#         print("Hello i am a method mentioned inside factory")


# class FactoryPune(FactoryMumbai):    #child class/ sub class
#     pass

# obj = FactoryPune()
# print(obj.a)
# obj.hello()


#02.
# class animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"hello your are {self.name}")

# class Human(animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#             print(f"hello your name is {self.name} and your age is {self.age}.")

# animal1 = animal("lion")
# animal1.show()
# person1 = Human("Sanskari",23)
# person1.show()


#03. 
# multiple inheritance
# class Animal:
#     name1 = "lion"

# class Human:
#     name2 = "harsh"

# class Robot(Animal, Human):
#     name3 = "X23dfd"

# obj = Robot()
# print(f"{obj.name1}, {obj.name2}, {obj.name3}")

#04. constructor function will be inherited of the first class that has been inherited. thid is mro(method resolution order)

# class Animal:
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robot(Animal, Human):
#     name3 = "X23dfd"

# obj = Robot()
# print(f"{obj.name1}, {obj.name2}, {obj.name3}")



#05.
#multilevel inheritance
class Factory:
    def __init__(self,material,zip):
        self.material = material
        self.zip = zip

    def show(self):
            print(f"this bag has {self.material}, and {self.zip} zip")

class BhopalFactory(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color = color
    def show(self):
            print(f"this bag has {self.material}, {self.zip} and {self.color} color.")

class PuneFactory(BhopalFactory):
    def __init__(self, material, zip, color,pockets):
        super().__init__(material, zip, color)
        self.pockets = pockets
    def show(self):
                    print(f"This bag has {self.material} material, {self.zip} zips, {self.color} color and {self.pockets} pockets.")


obj = PuneFactory("Cotton",3,"Black",4)
obj.show()