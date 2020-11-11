from plotnine.data import economics

from plotnine import ggplot, aes, geom_line, labs

g = ggplot(economics) + aes(x="date", y="uempmed") + geom_line() + labs(x="date", y="median duration of unemployment")

g.save("06.png")
