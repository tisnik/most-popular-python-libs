# naimportujeme vybrané funkce z knihovny `bokeh.plotting`
from bokeh.plotting import figure, output_file, show

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# barvová paleta
import palette_ice

# textura by měla být čtvercová a její šířka i výška by měla být
# mocninou čísla 2
IMAGE_WIDTH = 512
IMAGE_HEIGHT = 512

# matice představující bázi rastrového obrázku
image = np.empty((IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.uint32)

# "pohled" na matici jako na trojrozměrné pole
view = image.view(dtype=np.uint8).reshape((IMAGE_HEIGHT, IMAGE_WIDTH, 4))

# výběr barvové palety
palette = palette_ice.palette

# vyplnění obrázku vzorkem
for j in range(IMAGE_HEIGHT):
    for i in range(IMAGE_WIDTH):
        k = i * i + j * j
        val = int(k) & 255
        # aplikace barvové palety
        view[i, j, 0] = palette[val][0]  # red
        view[i, j, 1] = palette[val][1]  # green
        view[i, j, 2] = palette[val][2]  # blue
        view[i, j, 3] = 255  # alpha

# plocha pro graf
p = figure(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, x_range=(0, 10), y_range=(0, 10))

# vykreslení rastrového obrázku typu RGBA
p.image_rgba(image=[image], x=[0], y=[0], dw=[10], dh=[10])

# vykreslení grafu do plochy webové stránky
show(p)
