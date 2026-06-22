num = int(input("Enter number : "))
if num < 100:
    print(num , "is less than 100.")

    if num % 2 == 0:
        print(num , "is Even.")
        
    else:
        print(num , "is Odd.")

else:
    print(num , "is greater than 100.")