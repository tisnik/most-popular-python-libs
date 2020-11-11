from plotnine.data import mpg
from plotnine import ggplot, aes, geom_bar

g=(ggplot(mpg) + aes(x="class") + geom_bar())

g.save("12.png")
