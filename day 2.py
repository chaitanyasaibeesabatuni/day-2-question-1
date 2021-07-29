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


###################################program two ########################

#################checking string is panagram


string = input("Enter the string : ")
alpha = 'abcdefghijklmnopqrstuvwxyz'
if len(set(alpha) - set(string.lower()))==0:
    print("It's a pangram.")
else:
    print("It's not a pangram.")
