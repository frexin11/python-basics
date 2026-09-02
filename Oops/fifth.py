#---------------------------Encapsulation------------------------------#
# hiding the internal details of how things work and showing only what is needed.
# it keeps data safe from being changed by mistake.

# Capsule = attribute + method

class Factory:
    __city = "pune"    #private (double-underscore)

    # def __show(self):
    #     print(f"your city name is pune")

    def show(self):
        print(f"your city name is {Factory.__city}")

obj = Factory()
# print(obj.__city)
# obj.__show()
obj.show()



# 01.

# class Demo:
#     def __init__(self):
#         self.name = "Harsh"             #public
#         self._age = 23                  #protected
#         self.__salary = 45000           #private
#     def show(self):
#         print(self.name)
#         print(self._age)
#         print(self.__salary)

# obj = Demo()
# obj.show()