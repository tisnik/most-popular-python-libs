import matplotlib.pyplot as plt
import scipy.signal as signal

# filtr
win = signal.windows.hann(50)

# vykreslení výsledného signálu
plt.plot(win)

# uložení grafu s průběhem signálu
plt.savefig("window_1.png")

# zobrazení grafu
plt.show()
