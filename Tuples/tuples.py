 

my_tuple = (1,2,3)
another_tuple = 1,2,3
a= (1,)     # tuple
b=(1)       # not tuple

tuple_from_string = tuple('Hello')
print(tuple_from_string)

tuple_from_list = tuple([1,2,3])
print(tuple_from_list)

t = (1,[2,3])
t[1].append(4)
print(t)

original_tuple = (1,2,3)
new_tuple = original_tuple + (4,5)
print(new_tuple)    

#accessing tuple elements
my_tuple = (10,20,30,40,50)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
print(my_tuple[-1]) # Output: 50

#slicing
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[2:])   # Output: (30, 40, 50)
print(my_tuple[-3:-1]) # Output: (30, 40)
print(my_tuple[::2])  # Output: (10, 30, 50)


'''
tuple unpacking allows you to asssign tuple elements to individual variables in a single operation.
'''
t = (1, 2, 3)   
print(type(t))  # Output: <class 'tuple'>
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(a, b, c)  # Output: (1, 2, 3 )

a, *b = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: [2, 3]
print(a,b)  # Output: (1, [2, 3])
a, *b, c = 1, 2, 3, 4, 5, 6
print(a, b, c)  # Output: (1, [2, 3, 4, 5], 6)

a,b = [1,2]
print(a,b)  # Output: (1, 2)
a,*b = [1,2,3]
print(a,b)  # Output: (1, [2, 3])
a,*b,c = "Hello"
print(a,b,c)  # Output: ('H', ['e', 'l', 'l'], 'o')


