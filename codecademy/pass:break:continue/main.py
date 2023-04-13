#names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']


#The break keyword terminates a loop.
#break statements are typically found within conditional statements.
#If a certain condition is met, the loop stops iterating and breaks at that point.


#for name in names:
#    if 'h' in name.lower():
#       pass
#        break
#    else:
#        print(name)

names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']

for name in names:
    if 'm' in name.lower():
        continue
    elif 'r' in name.lower():
        pass
    elif 'j' in name.lower():
        break
    else:
        print(name)
