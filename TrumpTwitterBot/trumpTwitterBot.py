# Trump-Twitter-Bot

import random

part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]
part5 = ["Whitch-Hunt"]

# erstellen: Listen von Listen!
bestWords = [part1, part2, part3, part4, part5]
#print(bestWords[1])

sentence = []

for part in bestWords:
    r = random.randint(0, len(part) -1)
    sentence.append(part[r])
    
print(sentence)
print(' '.join(sentence) + '!')