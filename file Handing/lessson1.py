# f = open("superman.txt", 'r')
# print(f.mode)
# f.close()

with open("superman.txt",'r') as f:
    f_content = f.read()
    print(f_content)
