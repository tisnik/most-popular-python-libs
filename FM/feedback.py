# FM syntéza
#
# -zobrazení vlivu zpětné vazby mezi dvojicí operátorů v FM (PM) syntéze
# -založeno na vztahu: next_output = SIN(current_time + beta * previous_output)
# - pro vykreslení je použita knihovna Matplotlib

from math import sin

import matplotlib.pyplot as plt
import numpy as np

VALUES = 200

beta = 1.55

x = np.linspace(0, 10, VALUES)
y = np.zeros((VALUES,))

previous = 0
for i in range(VALUES):
    output = sin(i / 10.0 + beta * previous)
    y[i] = output
    previous = output


plt.plot(x, y)
plt.savefig("feedback.png")
plt.show()
