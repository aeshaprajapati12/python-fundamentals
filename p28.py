car_value = float(input("Enter the car value: "))
category = input("Enter category (A/B/C): ")

if category == "A" or category == "a":
    premium = car_value * 0.02

elif category == "B" or category == "b":
    premium = car_value * 0.03

elif category == "C" or category == "c":
    premium = car_value * 0.05
    
else:
    print("Invalid Category")
    premium = None

if premium is not None:
    print("Insurance Premium =", premium)