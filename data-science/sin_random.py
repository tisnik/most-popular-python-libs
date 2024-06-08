x1 = np.linspace(0, 4*np.pi, 100)
# hodnoty na y-ové ose: první funkce

y1 = np.sin(x1)
# hodnoty na y-ové ose: druhá funkce

import numpy.random as rnd

r = rnd.random(100) - 0.5

x2 = np.linspace(np.pi, 3*np.pi, 100)

y2 = np.sin(x2)+r
# vykreslit průběh obou funkcí

plt.plot(x1, y1, x2, y2)
# popis os

plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")
# zobrazení grafu

plt.show()
