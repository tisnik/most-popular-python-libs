from plotnine.data import mtcars
from plotnine import ggplot, aes, geom_bar, stat_bin

g=(ggplot(mtcars) + aes(x="hp") + stat_bin(bins=12) + geom_bar())

g.save("14.png")
