# for item in 'python':
# for item in ['John','Tylor','Sam']:
for item1 in range(4,9):  # range() is work like [4,9) = 4,5,6,7,8
    print(item1)
print("...............")
for item2 in range(4,9,2):  # here out put is(last 2 is work like step) = 4,6,8 
    print(item2)
print("...............")
price = [10,20,30]
sum = 0
for i in price:
    sum+=i
print(f"Total cost: ${sum}")