m1 = int(input('Enter 1st subject marks : '))
m2 = int(input('Enter 2nd subject marks : '))
m3 = int(input('Enter 3rd subject marks : '))
m4 = int(input('Enter 4th subject marks : '))
m5 = int(input('Enter 5th subject marks : '))


sum = m1 + m2 + m3 + m4 + m5
avg = sum / 5

if avg >= 90:
    grade = "A+"

elif avg >= 80 and avg <= 90:
    grade = "A"

elif avg >= 70 and avg <= 80:
    grade = "B"

elif avg >= 60 and avg <= 70:
    grade = "C"

elif avg >= 50 and avg <= 60:
    grade = "D"
    
else:
    grade = "F"

print("Result : Pass")
print("grade :",grade)
print("Total is :",sum)
print("Percentage is :",avg)
    


