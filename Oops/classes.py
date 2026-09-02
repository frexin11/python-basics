# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("moving")
    
#     def draw(self):
#         print("drawing")

# p1 = point(10, 20)
# print(p1.x)
# p1.move()
# p1.draw() 




# class Person:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(f"{self.name} is talking")

# p1 = Person("Sanyam")
# print(p1.name)
# p1.talk()

# p2 = Person("Rohan")
# p2.talk()




# class Student:
#     name ='Suraj'
#     rollno = 0
#     def __init__(self):
#         print("Constructor called")

# s1 = Student()
# s1.name = "Sanyam"
# s1.rollno = 1234
# print(s1.name)
# print(s1.rollno)




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Constructor called")

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e1 = Employee("Sanyam", 50000)
print(e1.name,e1.salary)

e2 = Employee("Rohan", 60000)
e2.show()