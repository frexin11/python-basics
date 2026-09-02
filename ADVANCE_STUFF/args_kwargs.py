# def addition(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(f"sum = {sum}")


# addition(12,23,16,76,23)

def information(**kwargs):
    # print(kwargs)
    for i in kwargs:
        print(f"{i} = {kwargs[i]}")

 
information(name = "Harsh", rollno =23, standard = 7, perentage = 86 )