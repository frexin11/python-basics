def greet_user(name):
    print(f"Hey {name}!")
    print("Welcome aboard")


print("Start")
name = "Nitin"
greet_user(name)
print("Finish")

#function that return value
def square(number):
    return number * number

number = int(input("Enter number: "))

print(square(number))


#emoji converter using a function
def emojiConverter(message):
    emojis ={
    ":)": "😀",
    ":(":"😞",   
    ":P":"😛",
    ";)":" 😉",
    ":/":"😕",

}
    output = ""
    words = message.split(" ")
    for word in words:
        output += emojis.get(word,word)+" "
    return output


message = input(">")
print(emojiConverter(message))



