#This python program prints the multiplication table of any given number

N = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{N} * {i} = {i * N}")