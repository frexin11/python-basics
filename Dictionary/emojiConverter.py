message = input(">")
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
print(output)


