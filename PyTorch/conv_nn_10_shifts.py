import matplotlib.pyplot as plt
import numpy as np

# číslice reprezentované v masce 8x8 pixelů
digits = (
    (0x00, 0x3C, 0x66, 0x76, 0x6E, 0x66, 0x3C, 0x00),
    (0x00, 0x18, 0x1C, 0x18, 0x18, 0x18, 0x7E, 0x00),
    (0x00, 0x3C, 0x66, 0x30, 0x18, 0x0C, 0x7E, 0x00),
    (0x00, 0x7E, 0x30, 0x18, 0x30, 0x66, 0x3C, 0x00),
    (0x00, 0x30, 0x38, 0x3C, 0x36, 0x7E, 0x30, 0x00),
    (0x00, 0x7E, 0x06, 0x3E, 0x60, 0x66, 0x3C, 0x00),
    (0x00, 0x3C, 0x06, 0x3E, 0x66, 0x66, 0x3C, 0x00),
    (0x00, 0x7E, 0x60, 0x30, 0x18, 0x0C, 0x0C, 0x00),
    (0x00, 0x3C, 0x66, 0x3C, 0x66, 0x66, 0x3C, 0x00),
    (0x00, 0x3C, 0x66, 0x7C, 0x60, 0x30, 0x1C, 0x00),
)


def digit_to_array(digits, n):
    digit = digits[n]
    rows = []
    # převod jednotlivých řádků na osmici bitů
    for scanline in digit:
        row = []
        # převod bitmapy představující řádek na osmici bitů
        for _ in range(8):
            bit = scanline & 0x01
            row.append(float(bit))
            scanline >>= 1
        rows.append(row)
    # transformace na n-dimenzionální pole
    return np.array(rows)


def shift(arr, x_shift, y_shift):
    # horizontální posun
    arr = np.roll(arr, x_shift, axis=1)

    # výplně těch částí, které byly orotovány na druhou stranu
    if x_shift < 0:
        arr[:, x_shift:] = 0.0
    elif x_shift > 0:
        arr[:, :x_shift] = 0.0

    # vertikální posun
    arr = np.roll(arr, y_shift, axis=0)

    # výplně těch částí, které byly orotovány na druhou stranu
    if y_shift < 0:
        arr[y_shift:] = 0.0
    elif y_shift > 0:
        arr[:y_shift] = 0.0
    return arr


# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 6.4))
plt.axis("off")

i = 1
for y_shift in range(-2, 3):
    for x_shift in range(-2, 3):
        array = digit_to_array(digits, 2)
        array = shift(array, x_shift, y_shift)
        ax = plt.subplot(5, 5, i)
        i += 1
        ax.matshow(array)

# převod na stupně šedi
plt.gray()

# uložení vizualizované matice
plt.savefig("conv_nn_10.png")

# vizualizace matice na obrazovce
plt.show()
