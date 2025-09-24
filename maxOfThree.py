#Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.

A = int(input("Enter A number: "))
B = int(input("Enter B number: "))
C = int(input("Enter C number: "))

if A==B==C:
    print(A)
else:
    print(max(A,B,C))