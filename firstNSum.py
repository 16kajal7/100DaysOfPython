#This program finds the sum of first N natural numbers

N = int(input("Enter a number: "))
total = 0

for i in range(0,N+1):
    total = total + i
print("The sum of first N natural number's is ",total)