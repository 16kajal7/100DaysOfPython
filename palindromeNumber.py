#This python program checks if a number is palindrome or not

N = input("Enter the number: ")

if N == N[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")