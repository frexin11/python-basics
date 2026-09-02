print("welcome to the quiz game")
playing = input("Do you want to play? (Yes/No) ")
score = 0
if playing.lower() != "yes":
    quit()
print("okay! lets play :)")   
answer = input("How types of inheritance? ")
if answer == "4":
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print('correct!')
    score += 1
else:
    print('wrong!') 
answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('wrong!')
answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('wrong!')     
answer = input("What is the full form of PSU? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print('wrong!') 
print(f"you got {score}/5 questions correct!")
