import random
#random() erzeugt eine Zufallszahl zw. 0 & 1
#a = random.random()
#print(a)
#randit(1,6) erzeugt eine Zufallszahl zw. 1 & 6
#b = random.randint(1, 6)
#print(b)

counter = 0
number = 0
while number != 6:
    number = random.randint(1, 6)
    counter += 1

print("Es wurden " + str(counter)
      + " Würfe benötigt um eine 6 zu Würfeln")


