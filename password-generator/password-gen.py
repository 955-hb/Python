import random

pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', '0', ' ', '!', '@', '#', '$', '%', '<', '>', '(', ')', '/', '&', '?', '=', '"',
         ]

#declairing the empty string
password = ""

#loop to generate the random password of the length entered by the user
for x in range(10):
    password = password + random.choices(pass1)[0]
print('youre new password is:\n', password)