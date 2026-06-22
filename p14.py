age = int(input("Enter age : "))
if age > 18:
    print("Eligible for blood donate.")

    if age > 55:
        print("Not eligible for blood donate.")

age = int(input("Enter your age: "))

if age > 18 and age <= 55:
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")