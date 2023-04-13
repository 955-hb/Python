import random

roundsWon = 0
roundsToPlay = 10

for x in range(roundsToPlay):
    print("Geben Sie eine Zahl zw. 1 & 10 ein:")
    guess = int(input())
    number = random.randint(1, 10)

    if guess == number:
        roundsWon += 1
        print("Glückwunsch! Sie haben richtig geraten!")
    else:
        print("Leider falsch! Die Zahl war {}" .format(number))

print("\n\n_____________________________\n"
      + "Spiel beendet\n"
      + "Gewonnene Runden: %s von %s Runden" % (roundsWon, roundsToPlay))


