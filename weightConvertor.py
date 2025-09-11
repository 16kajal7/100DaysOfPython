# This python programs asks user to enter their weight in either kilograms or pounds, and then
# it converts it to other unit and print

weight = input("Enter your weight in either Kilograms or Pounds: ")
unit = float(input("Enter the unit of your weight: "))

if weight == "K" or weight=="k":
    unit = unit * 2.20462
    print(f"Your weight is {unit} pounds")
elif weight == "L" or weight=="l":
    unit = unit / 2.20462
    print(f"Your weight is {unit} kilograms")

