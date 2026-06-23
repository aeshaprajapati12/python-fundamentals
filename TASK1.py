'''Take 3 Numbers from User Store in List and Print List Asc Order'''

numbers = []
for i in range(3):
    num = int(input("Enter the number : "))
    numbers.append(num)

numbers.sort()
print(numbers)

print("\n")

'''
Create Marksheet Program using List
Take 5 Numbers,Print Total,Print % and Print Grade
'''

marks = []
for i in range(5):
    mark = int(input("Enter Marks : "))
    marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

print("Marks:", marks)
print("Total =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)

print(marks)


print("\n")

'''
Create Marksheet Program using Tuple
Take 5 Numbers,Print Total,Print % and Print Grade
'''

marks = []
for i in range(5):
    mark = int(input("Enter Marks : "))
    marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

print("Marks:", tuple(marks))
print("Total =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)

print(marks)

print(tuple(marks))

print("\n")


'''
Create Marksheet Program using Dict
Take 5 Numbers,Print Total,Print % and Print Grade
'''

marks = {}

for i in range(1, 6):
    marks[f"Subject {i}"] = int(input(f"Enter marks for Subject {i}: "))

total = sum(marks.values())
percentage = total / 5

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 50:
    grade = "D"

else:
    grade = "F"

print("\nMarksheet")
print("Marks:", marks)
print("Total =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)

