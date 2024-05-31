# Gehaltsrechner

stundenlohn = input('Bitte geben Sie Ihren Stundenlohn ein: ')
tag = (8 * int(stundenlohn))
monat = tag * 20
jahr = monat * 12

print('dein Stundenlohn beträgt: ' + str(stundenlohn) + '€!')
print('Dein Tageslohn beträgt: ' + str(tag) + '€!')
print('Dein Monatslohn beträgt: ' + str(monat) + '€!')
print('Dein Jahreslohn beträgt: ' + str(jahr) + '€!')





input('drücken Sie eine beliebige Taste zum beenden des Programms.')