# syntax error :-apple

# print("hello, Frexin)
# SyntaxError: unterminated string literal
# print("Hello, World") # correct one

#ValueError:-
# x= int(input("what is x? "))
# print(f"x is {x}") #Give input 'cat' and check
# ValueError: invalid literal for int() with base 10: 'cat'
#  solution:-

#method 1
# try:
#     x= int(input("what is x? "))
#     print(f"x is {x}")
# except ValueError: 
#     print("x is not an integer")

#method 2
# try:
#     x= int(input("what is x? "))
# except ValueError: 
#     print("x is not an integer")
# #print(f"x is {x}")  # NameError: name 'x' is not defined to solve this use else
# else:
#     print(f"x is {x}")  

#method 3
# while True:
#     try:
#         x= int(input("what is x? "))
#     except ValueError: 
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}") 

#method 4 
def main():
    x= get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what is x? "))
            return x
        except ValueError:
            # print("x is not an integer")
            pass

main()