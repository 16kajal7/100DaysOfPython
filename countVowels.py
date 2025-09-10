#This python program counts number of vowels in a string

string = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U"]
count = 0

for char in string:
    if char in vowels:
        count = count + 1
print("Number of vowels are: ",count)
