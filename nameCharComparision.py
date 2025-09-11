#This python program finds whether name is less than 3 characters long then it prints
# name must be at least 3 characters and if the name is more than 50 characters long
# then prints name must be maximum of 50 characters otherwise name looks good

name = str(input("What is your name? "))

if len(name) < 3:
    print("Name must be 3 characters at least")
elif len(name) > 50:
    print("Name must be maximum of 50 characters")
else :
    print("Name looks good")
