# Pie Chart mit Hilfe von Mathplotlib


# import von Mathplotlib
import matplotlib.pyplot as plt

# definieren der jeweiligen Label
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [ 45, 22, 18, 15]


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90) # %1.1f%% --> definiert das %-Zeichen
plt.title('Pie-Chart')
plt.show()
