# Stein Schere Papier
import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

TIE = "Tie"
WIN = "you Win"
LOSE = "you Lose :( "

def compare_moves(you, computer):
    if you == computer:
        return TIE
    elif you == SCISSORS and computer == PAPER:
        return WIN
    elif you == ROCK and computer == SCISSORS:
        return WIN
    elif you == PAPER and computer == ROCK:
        return WIN
    else:
        # ... in allen anderen Fällen
        return LOSE

you = ""

while you not in [ROCK, PAPER, SCISSORS]:
    you = input("(r)rock, (p)paper, or (s)scissors? > ")

computer = random.choice([ROCK, PAPER, SCISSORS])
result = compare_moves(you, computer)

print(f"YOU: {you}, Computer: {computer}. {result}")


