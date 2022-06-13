# naimportujeme vybrané funkce z knihovny `bokeh.plotting`
from bokeh.plotting import figure, show

factors = ["a", "b", "c"]
x = ["a"] * 3 + ["b"] * 3 + ["c"] * 3
y = factors * 3

print(factors)
print(x)
print(y)

# barvy jednotlivých čtverečků
colors = [
    "#0B486B",
    "#79BD9A",
    "#CFF09E",
    "#79BD9A",
    "#0B486B",
    "#79BD9A",
    "#CFF09E",
    "#79BD9A",
    "#0B486B",
]

# plocha pro graf
p = figure(
    title="Categorical Heatmap",
    tools="hover",
    toolbar_location=None,
    x_range=factors,
    y_range=factors,
)

# vykreslení heatmapy
p.rect(x, y, color=colors, width=1, height=1)

# vykreslení grafu do plochy webové stránky
show(p)
