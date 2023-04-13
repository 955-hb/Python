import random

guess = input("Your guess (1-10): ")
lucky_number = random.randint(1, 10)

if int(guess) == lucky_number:
    print("You win!")
else:
    print(f"You lose. Lucky number is {lucky_number}")
