#attribute and methodds
class  Animal:
    name = "lion"                #class attribute

    def __init__(self,age):     #instance attribute
        self.age = age

    def show(self):                 #instance method
        print(f"hello, this animal age is {self.age}")

    @classmethod
    def hello(cls):
        print("this planet")

    @staticmethod
    def static():
        print("earth, Jupiter")


obj = Animal(34)
obj.show()

obj.hello()
obj.static()