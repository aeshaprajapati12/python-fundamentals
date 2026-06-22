m1 = int(input('Enter 1st subject marks : '))
m2 = int(input('Enter 2nd subject marks : '))
m3 = int(input('Enter 3rd subject marks : '))
m4 = int(input('Enter 4th subject marks : '))
m5 = int(input('Enter 5th subject marks : '))

if m1 <= 18 or m2 <= 18 or m3 <= 18 or m4 <= 18 or m5 <= 18:
    print("Result : Fail")

else:
    sum = m1 + m2 + m3 + m4 + m5
    avg = sum / 5

    if avg >= 80:
        grade = "A"

    elif avg >= 70:
        grade = "B"

    elif avg >= 60:
        grade = "C"

    elif avg >= 50:
        grade = "D"
    
    else:
        grade = "E"

    print("Result : Pass")
    print("grade :",grade)
    print("Total is :",sum)
    print("Percentage is :",avg)
    


