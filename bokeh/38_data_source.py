# naimportujeme vybrané funkce z knihovny `bokeh.plotting`
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# jména na X-ové ose
languages = ["Python", "C++", "C#", "Visual Basic", "JavaScript", "SQL", "Assembly", "Java", "C", "Swift"]

# hodnoty na Y-ové ose
ratings = [12.20, 9.63, 6.12, 5.42, 2.09, 1.94, 1.85, 10.47, 11.91, 1.55]

# definice zdroje dat
source = ColumnDataSource(data=dict(languages=languages, ratings=ratings))

# plocha pro graf
p = figure(x_range=languages, height=250, title="TIOBE index",
           toolbar_location=None, tools="")

# vykreslení průběhu hodnot
p.vbar(x='languages', top='ratings', source=source, width=0.9)

# styl vykreslení
p.xgrid.grid_line_color = None
p.y_range.start = 0

# vykreslení grafu do plochy webové stránky
show(p)
