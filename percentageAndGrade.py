#Write a program to calculate the percentage (according to marks of a student) and grade (according to the
# percentage of a student). Five numbers(A, B, C, D & E) represent the marks of a student in 5 subjects which are out
# of 100. Print the percentage and the grade of the student.

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

total = A + B + C + D + E
percentage = (total / 500) * 100
percentage = int(percentage)

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(percentage)
print(grade)
