import scipy.datasets as datasets
from scipy import fftpack

import numpy as np

# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

np.info(ascent_fft)

a = np.abs(ascent_fft)
print(np.min(a))
print(np.max(a))

