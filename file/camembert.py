import matplotlib.pyplot as plt
import numpy as np
import sys

result=[]
cpt=0
for line in sys.stdin:
    niveau, formation, filiere, inscrit = line.split(',')
    result.append((filiere, int(inscrit)))
    print(cpt, niveau, formation, filiere)
    cpt= cpt +1

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(10,10))

header = tuple(i[0] for i in result)
values = tuple(i[1] for i in result)

ax.pie(values, labels=header, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Filière les plus demandé:')

plt.show()