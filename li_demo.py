mylist = [10,10.5,"Aesha",10.99999]
print(mylist)
print(type(mylist))

print(mylist[0])
print(mylist[0 : 2])
print(mylist[ : 3])
print(mylist[2 : 4])
print(mylist[1 : ])
print(mylist[ : -1])
print(mylist[-1 : -3])
print(mylist[-1 : ])

print(mylist[0])
mylist[0] = 29
print(mylist)


print("\n\n")

mylist1 = []

count = int(input("Enter number of data : "))

for i in range(count):
    value = input("Enter data : ")
    mylist1.append(value)

print(mylist1)
print("Length of the list is : " ,len(mylist1))


print("\n\n")

concatli = mylist1 + mylist
print(concatli)

concatli1 = mylist * 2
print(concatli1)

print("\n\n")


mylist2 = [10,29.5,"Prajapati",99.99999]
index = 0

for myval in mylist2:
    print("Index is : " , index , "Value is : " , myval)
    index += 1

print(mylist2)

print("\n\n")