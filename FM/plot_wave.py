#
#  (C) Copyright 2024, 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#

# Zobrazení průběhu audio signáku přečteného ze souborů typu WAV

import wave

import matplotlib.pyplot as plt
import numpy as np

with wave.open("opl2-4.wav", "rb") as f:
    buffer = f.readframes(f.getnframes())
    interleaved = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
    data = np.reshape(interleaved, (-1, f.getnchannels()))
    print(data.shape)   # zobrazit počet samplů a kanálů
    data = data[:,0]    # první kanál
    plt.plot(data[60500:61000])  # malý výřez
    plt.show()
