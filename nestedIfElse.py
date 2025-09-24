# #This python program shows nested if-else. Given the number N, Categorise the number according to following condition:
# 1. Odd-Positive
# 2. Odd-Negative
# 3. Even-Positive
# 4. Even-Negative

Num = int(input("Enter a number: "))

if Num % 2 == 0:
    if Num >= 0:
        print("Even-positive")
    else:
        print("Even-negative")
elif Num % 2 != 0:
    if Num >= 0:
        print("Odd-positive")
    else:
        print("Odd-negative")