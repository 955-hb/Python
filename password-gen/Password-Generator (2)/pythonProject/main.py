print('Generate your new Password.')

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!§$%&?*/+#_-:;@€{[]}<>'

allChars = lower + upper + numbers + symbols
length = int(input('Wie lang soll der Block sein? '))

passwordOne = (''.join(random.sample(allChars, length))) + ' - ' + (''.join(random.sample(allChars, length))) + ' - ' + (''.join(random.sample(allChars, length)))
passwordTwo = (''.join(random.sample(allChars, length))) + ' - ' + (''.join(random.sample(allChars, length)))
passwordThree = ''.join(random.sample(allChars, length))

print('Dein neues Password lautet: ')
print(' ')
print(passwordOne)
print(' ')
print(passwordTwo)
print(' ')
print(passwordThree)
print(' ')


input('drücken Sie eine beliebige Taste zum Beenden des Programmes!')
