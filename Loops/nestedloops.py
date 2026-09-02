# for i in range(4):
#     for j in range(3):
#         print(f'({i}, {j})')


number = [5,2,5,2,2]
# xxxxx
# xx
# xxxxx
# xx
# xx

for i in number:
    output = " "
    for j in range(i):
        output+="I"
    print(output)