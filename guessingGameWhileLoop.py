# This python program asks user to guess a secret number 9 for upto 3 chances
# using while loop

secret_number = 9
guess_chance = 0
guess_limit = 3
while guess_chance < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_chance = guess_chance + 1
    if guess == secret_number:
        print("You guessed right!")
        break
else :
    print("Sorry, you lose")