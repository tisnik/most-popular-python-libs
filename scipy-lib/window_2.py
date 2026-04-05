import scipy.signal as signal

import matplotlib.pyplot as plt

# filtr
win = signal.windows.triang(50)

# vykreslení výsledného signálu
plt.plot(win)

# uložení grafu s průběhem signálu
plt.savefig("window_2.png")

# zobrazení grafu
plt.show()
