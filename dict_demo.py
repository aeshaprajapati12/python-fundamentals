mydic = {1 : "aesha , prajapati" , 2 : 2 , 'A' : 13 , "B" : "Apple" }
print(mydic)
print(type(mydic))

print("\n\n")

print(mydic['A'])
print(mydic[1])
mydic[2] = "python"
print(mydic)

print("\n\n")

index = 0
for x in mydic:
    print("my index is : " , index , " Key is : " , x , " value is : " , mydic[x])
    index+=1

print("\n\n")

for y in mydic.keys():
    print(y)
print("\n")

for z in mydic.values():
    print(z)
print("\n")

for s in mydic.items():
    print(s)
print("\n")