class Dog:
    def walk(self):
        print("walk")

    def sound(self):
        print("bark")


class Animal(Dog):
    pass


class Cat(Animal):
    def sound(self):
        print("meow")


c1 = Cat()
c1.walk()
c1.sound()

a1 = Animal()
a1.walk()
a1.sound()