# Method - 1
li = [int(i) for i in input("Enter values : ").split()]
lis = []
for i in li:
    if i not in lis:
        lis.append(i)
print(lis)

#Method - 2
#Using Set Data Structure
li = [int(i) for i in input("Enter values : ").split()]
li = set(li)
print(li)