#This program finds if a given year is a leap year or not

i = int(input("Enter the year: "))

if i%4==0 and i%100!=0 or i%400==0:
    print(i,"is a leap year")
else:
    print(i,"is not a leap year")