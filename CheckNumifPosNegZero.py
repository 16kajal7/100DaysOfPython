#This program checks if a number is positive, negative or a zero

num = int(input("Enter a number to check whether it's a positive, negative or a zero: "))

if num < 0:
    print("The given number is negative")
elif num == 0:
    print("The given number is zero")
else:
    print("The given number is positive")