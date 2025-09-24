#This python program prints right aligned *(star) triangle pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows-i) + '*' * i)
