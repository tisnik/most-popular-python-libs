from plotnine.data import economics

from plotnine import ggplot, aes, geom_line

ggplot(economics) + aes(x="date", y="pop") + geom_line()
