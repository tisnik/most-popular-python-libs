# Zobrazení průběhu audio signáku přečteného ze souborů typu WAV

import matplotlib.pyplot as plt
import numpy as np
import wave


with wave.open("opl2-4.wav", "rb") as f:
    buffer = f.readframes(f.getnframes())
    interleaved = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
    data = np.reshape(interleaved, (-1, f.getnchannels()))
    print(data.shape)   # zobrazit počet samplů a kanálů
    data = data[:,0]    # první kanál
    plt.plot(data[60500:61000])  # malý výřez
    plt.show()
