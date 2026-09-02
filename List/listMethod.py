numbers = [5,2,1,8,4,7]
print(f'original: {numbers}')
numbers.append(18)
print(f'after append: {numbers}')
numbers.insert(3,5)
print(f'after insert : {numbers}')
numbers.remove(7)
print(f'after remove: {numbers}')
# numbers.clear()               # it remove all element from list
numbers.pop()
print(f'after pop: {numbers}')
print("it show the index of 2 :",numbers.index(2))
print(40 in numbers)          # it check T/F whether value is present or not
print(numbers.count(5))       # output 2 because it count repetation of given number
numbers.sort()
# print(numbers)
numbers.reverse()
# print(numbers)

num = numbers.copy()
numbers.append(18)
print("its a copy : ",num)
print("its original after some change : ",numbers)




