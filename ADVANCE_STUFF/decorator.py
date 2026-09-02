#1. Decorator 
# def decorate(func):
#     def wrapper():
#         print("###################################")
#         func()
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#     return wrapper

# @decorate
# def hello():
#     print("Hello from NASA Sapce-Station.")

# hello()


# 2.
def decorate(func):
    def wrapper(a,b):
        print(f"The is a addition of {a} and {b}")
        func(a,b)
        print("Thank You, Hope you like it!")

    return wrapper

@decorate
def addition(a,b):
    print(f"sum of  2 number is {a+b}")

addition(45,18)



