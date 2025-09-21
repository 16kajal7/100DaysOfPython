#This python program swaps two numbers without using a third variable

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

a,b = b,a
print(f"{a} is first now and {b} is second!")