#This python program checks if the temperature is greater than 30
# then it's a hot day , if it is less than 30 then it's a cold day
# otherwise it's neither hot nor cold

temp = int(input("Enter the temperature: "))

if temp>30:
    print("It's a hot day")
elif temp<30:
    print("It's a cold day")
else:
    print("It's neither cold nor hot day")