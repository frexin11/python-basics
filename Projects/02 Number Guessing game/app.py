#number guessing game
import random
print("welcome to the number guessing game")
number = random.randint(1, 10)
guess = 0
count = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    count += 1
    if guess < number :
        print("too low!")
    elif guess > number :
        print("too high!")
    else:
        print("you guessed it right!")
print(f"you took {count} guesses!")