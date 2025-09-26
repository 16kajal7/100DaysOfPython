#Write a program that takes in a number N as input and does the following:
# if N is a multiple of 3, print Fizz
# if N is a multiple of 5, print Buzz
# if N is a multiple of both 3 and 5, print FizzBuzz

N = int(input())

if N % 3 == 0 and N % 5 == 0:
    print("FizzBuzz")
elif N % 3 == 0:
    print("Fizz")
elif N % 5 == 0:
    print("Buzz")