# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show, save

# hodnoty na x-ové a y-ové ose
x = range(10)
y = [1, 2, 7, 7, 4, 5, -5, 0, 2, 1]

# plocha pro graf
p = figure()

# vykreslení průběhu
p.line(x, y)

# vykreslení grafu do plochy webové stránky
show(p)
