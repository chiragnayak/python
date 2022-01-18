import random

my_number = random.randint(1, 100)

print("Guess the number..")
guess = -1

while guess != my_number:
    guess = int(input("Enter your number : "))
    if guess > my_number:
        print("Your Guess is greater than my number..")
    elif guess < my_number:
        print("Your Guess is lesser than my number...")
    else:
        print("WoW! You guessed it correctly. It is indeed {}".format(my_number))
