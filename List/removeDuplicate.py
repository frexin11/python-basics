# write a program to remove duplicates in a list
numbers = [3,8,9,2,4,7,3,4,8]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print (uniques)
uniques.sort()
print(uniques)
