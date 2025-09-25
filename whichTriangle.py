#Write a program to input from user three numbers(A, B & C) representing side lengths of a triangle.
#You have to print if the triangle is "equilateral", "scalene" or "isosceles".

A, B, C = map(int, input().split())

if A + B > C and B + C > A and C + A > B:
    if A == B == C:
        print("equilateral")
    elif A == B or B == C or C == A:
        print("isosceles")
    else:
        print("scalene")