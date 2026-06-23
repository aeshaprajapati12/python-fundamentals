mytuple = (10,"Aesha",22.12,99.99999)
print(mytuple)
print(type(mytuple))

mylist = [10,"Aesha",22.12,99.99999]
print(tuple(mylist))
print(type(mylist))


print(mytuple[0])
print(mytuple[0 : 2])
print(mytuple[ : 3])
print(mytuple[2 : 4])
print(mytuple[1 : ])
print(mytuple[ : -1])
print(mytuple[-1 : -3])
print(mytuple[-1 : ])

print(mytuple[0])
mytuple[0] = 29
print(mytuple)