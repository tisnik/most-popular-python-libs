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


def add_noise(array, level):
    return (1.0 - level) * array + level * np.random.rand(8, 8)


# velikost obrázku s grafem
plt.subplots(figsize=(3.2, 9.8))
plt.axis("off")

for j, digit in enumerate([5, 6, 8]):
    for i in range(1, 12):
        level = (i - 1.0) / 12.0
        array = digit_to_array(digits, digit)
        array = add_noise(array, level)
        ax = plt.subplot(12, 3, j + 1 + i * 3)
        ax.matshow(array)
        ax.axis("off")


# uložení vizualizované matice
plt.savefig("conv_nn_08.png")

# vizualizace matice na obrazovce
plt.show()
