#---------------------------Polymorphism-------------------------------#
# A same name having many differnrt form.
# method overriding
# class animal:
#     def show(self):
#         print("hello from animal")

# class human(animal):
#     def show(self):
#         print("hello from human")

# obj = human()
# obj.show()


# Duck typing
class animal:
    def show(self):
        print("HII")

class human:
    def show(self):
        print("HELLO")

obj1 = human()
obj1.show()

obj2 = animal()
obj2.show()