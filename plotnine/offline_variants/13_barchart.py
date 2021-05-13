from plotnine.data import mpg
from plotnine import ggplot, aes, geom_bar

g = (ggplot(mpg) + aes(x="cyl") + geom_bar())

g.save("13.png")
