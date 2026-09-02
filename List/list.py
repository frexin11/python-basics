# A built in ds that stores an ordered, mutable collection of items
# List can contain items of any types, including other lists

# Ordered = items have a defined order, and that order will not change unless you explicitly reorder the list.
# Mutable = items can be added, removed, or changed after the list has been created. 
# Heterogeneous = items can be of different types (e.g., integers, strings, other lists, etc.) within the same list.
# iterable = List can be looped over (iterated) using loops or comprehensions.

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.14, [1, 2, 3], True]
nested_list = [[1, 2], [3, 4], [5, 6]]

#empty list
empty_list = []

#list of strings
fruits = ["apple", "banana", "cherry", "date"]

#list of integers
numbers = [10, 20, 30, 40, 50]
 
 #list of booleans
bool_list = [True, False, True, False]

#list of mixed data types
mixed_data = [42, "Hello", 3.14, [1, 2, 3], True]


li = list()                 #  []
print(type(li))             # output = <class 'list'>

li = list("Hello")         #  ['H', 'e', 'l', 'l', 'o']
print(li)

s= {10,20,30,40,50}
print(list(s))              # output = [10, 20, 30, 40, 50]

print(list(range(5)))       # output = [0, 1, 2, 3, 4]

original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)  # creates a new list with the same elements
print(copied_list)          # output = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry", "date", "orange", "grape" ]
print(fruits[0])           # output = apple
print(fruits[-1])          # output = grape

# list [start:stop:step]
print(fruits[1:4])        # output = ['banana', 'cherry', 'date']
print(fruits[::2])        # output = ['apple', 'cherry', 'orange']
print(fruits[::-1])       # output = ['grape', 'orange', 'date', 'cherry', 'banana', 'apple']   
print(fruits[2:])         # output = ['cherry', 'date', 'orange', 'grape']
print(fruits[:3])         # output = ['apple', 'banana', 'cherry']
print(fruits[-3:])        # output = ['date', 'orange', 'grape']
print(fruits[:-1])        # output = ['apple', 'banana', 'cherry', 'date', 'orange']
print(fruits[1::2])       # output = ['banana', 'date', 'grape']

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])       # output = [20, 30, 40]
print(numbers[::2])       # output = [10, 30, 50]
print(numbers[::-1])      # output = [50, 40, 30, 20, 10]

numbers[1:4] = [25, 35, 45]      # it replace the value at given index
print(numbers)                   # output = [10, 25, 35, 45, 50]

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")         # it add element at the end of list
print(fruits)                   # output = ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape")       # it add element at specific index
print(fruits)                   # output = ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits2 = ["kiwi", "melon"]
fruits.extend(fruits2)          # it add multiple element at the end of list
print(fruits)                   # output = ['apple', 'grape', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

fruits.remove("banana")         # it remove specific element from list
print(fruits)                   # output = ['apple', 'grape', 'cherry', 'orange', 'kiwi', 'melon']
fruits.pop()                    # it remove last element from list
print(fruits)                   # output = ['apple', 'grape', 'cherry', 'orange', 'kiwi']

fruits.pop(-2)                  # it remove element at specific index (default -1)
print(fruits)                   # output = ['apple', 'grape', 'cherry', 'kiwi']

del fruits[1]                   # it remove element at specific index
print(fruits)                   # output = ['apple', 'cherry', 'kiwi']
del fruits[1:]                   # it remove element from specific index to end index (exclusive)
print(fruits)                   # output = ['apple']


fruits.clear()                  # it remove all element from list



print(len([1,2,3,[4,5]]))          # output = 4
numbers = [10, 20, 30, 40, 50]
print(min(numbers))             # output = 10
print(max(numbers))             # output = 50
print(sum(numbers))             # output = 150

names = ['Rdr 2','Death standing','Cyberpunk 2077','Gta v','God of war','Eldian ring','Watch dog legion']
print(min(names))              
print(max(names))   

usernames = ['alice', 'Alice', 'bob', 'Bob', 'charlie', 'Charlie']   
print(min(usernames))          # output = 'Alice' (uppercase letters come before lowercase letters in ASCII)
print(max(usernames))          # output = 'charlie' (lowercase letters come after uppercase letters in ASCII)   

print(ord('A'),ord('a'))                 # output  A=65 a=97


a  = [10, 20, 30]
b = [40, 50]
result = a + b
print(result)                   # output = [10, 20, 30, 40, 50]



# list methods append(), insert(), extend(), remove(), pop(), clear(), len(), min(), max(), sum(), sort(), reverse(), count(), index(), sorted(),reversed() copy(), etc.



fruits = ["apple", "banana", "cherry"]
# fruits.sort(key=none, reverse=False)   # it is default 
fruits.sort(key=len,reverse=True)        # it sort the list in reverse order based on length of string
print(fruits)                            # output = ['banana', 'cherry', 'apple']



print(sorted(fruits, key=len))                      # output = ['apple', 'banana', 'cherry']
nums= [-5, -3, -4, -2, -8, -1]
nums.sort(key=abs, reverse=False)           
print(nums)                   # output = [-1, -2, -3, -4, -5, -8]



for fruit in fruits:
    print(fruit)              # output = banana cherry apple


for i in range(len(fruits)):
    print(fruits[i])          # output = banana cherry apple



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')              
    print()    


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a),id(b))         # output = different memory address because they are different objects
print(a == b)              # output = True
print(a is b)              # output = False

b=a
print(id(a),id(b))         # output = same memory address 
print(a is b)              # output = True


li = [1,2,3,4,5,6]
res=[]
for i in li:
    res.append(i**2)
print(res)                   # output = [1, 4, 9, 16, 25, 36]

#list comprehension = [expression for item in iterable]
result = [i**2 for i in li]
print(result)                # output = [1, 4, 9, 16, 25, 36]


# find the maximum number in list without using max function
# numbers = [3,7,16,9,85,34,51]
# max = numbers[0]
# i=1
# while i<len(numbers):
#     if numbers[i]>max:
#         max = numbers[i]
#     i+=1    
# print("Maximum Number is : ",max)