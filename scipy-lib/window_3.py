import matplotlib.pyplot as plt
import scipy.signal as signal

# filtr
win = signal.windows.lanczos(50)

# vykreslení výsledného signálu
plt.plot(win)

# uložení grafu s průběhem signálu
plt.savefig("window_3.png")

# zobrazení grafu
plt.show()
