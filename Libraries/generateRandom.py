import random
for i in range(3):
    print(random.random())      #the random() method returns a random float number between 0.0 to 1.0
     
print(random.randint(1, 10))        #the randint() method returns a random integer number between the given range (inclusive)
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(random.choice(fruits)) #the choice() method returns a random element from the specified sequence (list, tuple, string, etc.)

print(random.sample(range(1, 100), 5)) #the sample() method returns a list of unique random elements from the specified sequence or range. The first argument is the population (the range of numbers), and the second argument is the number of elements to return.