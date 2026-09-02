str1 = 'Power Ranger Dino Thunder'
# str2 = 'Hii my name is "MAXIMUS"'
# str3 = "Shreya's dog is very angry now"
# str4 = '''
# Hii john,

# Here is our first email to you.

# Thank You,
# The Support Team

# '''

# print(str1)
# print(str2)
# print(str3)
# print(str4)

print(str1[0])    # P
# if we give neagative index result is print staring from End
print(str1[-1])   # [-1] print last char in string in py = r
print(str1[-2])   # e
print(str1[0:4])  # it print from [0 to 4) = Powe
print(str1[1:])   # print [1 to end = ower Ranger Dino Thunder
print(str1[:5])   # print [0 to 5) = Power

temp = str1[:]    # Print star to end or we say copy the whole string
print(temp)

name = 'Jeniffer'
print(name[1:-1])      # output = eniffe
