# i =1
# while i<=5:
#     print('*' * i)
#     i+=1
# print("Done")

value = 9
guessCount = 0 
guessLimit = 3
print("You have 3 maximum limit to guess a number b/w 1 to 9")
while guessCount < guessLimit:
    guessNumber = int(input("Guess: "))
    guessCount+=1
    if value == guessNumber:
        print('You Won!')
        break
    # elif guessCount >=guessLimit:
    #     print("Game Over")
    # else:
    #     print("Wrong Guess")
else:
    print("Game Over!")   

    
