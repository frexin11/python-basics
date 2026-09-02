# student={
#     "name":"John Snow",
#     "age":24,
#     'grade':'A',
#     'marks':'84',
#     "is_verified": True
# }
# student['name'] = "Arya Stark"
# del student['grade']
# print(student.pop('grade'))       # it will remove the key and return the value
# print(student.popitem())          # it will remove the last inserted key and return the key and value as tuple
# print(student['name'])
# print(student.get("age"))
# print(student.get("birthday","jan 1st 2002"))


# number ={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# input_number =input("Phone: ")
# for ch in input_number:
#    output+= number.get(ch,"!")+" "
# print(output)

'''
dictionary_name={
    key:value,
    key:value,
    key:value
}
'''
from operator import index


fruits={
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grapes":"green",
    "watermelon":"green"
}
print("vic",end="....\n")
dict(apple = "red",banana="yellow",orange = "orange",kiwi="brown")

d= dict([("apple","red"),("banana","yellow"),("orange","orange"),("kiwi","brown")])
print(d)


#Hash Table -> special type of araay 
#
student={
    "name":"John Snow",
    "age":24,
    'grade':'A',
}
print(hash("name"))

index =hash("name")%8
print(index)

index =hash("age")%8
print(index)

index = hash("grade")%8
print(index)

student={
    "Soni" : 79,
    "Rohan" : 83,
    "Suraj" : 99,
    "Nitin" : 89,
}
input_name = input("Enter name:")
print(student.get(input_name.title(),"Not found"))