from plotnine.data import economics
from plotnine import ggplot, aes, geom_bar, stat_bin

g=(ggplot(economics) + aes(x="uempmed") + stat_bin(bins=20) + geom_bar())

g.save("15.png")
