#This program finds the sum of digits of a given number n

n = int(input("Enter the number: "))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print ("The sum of digits is:",total)