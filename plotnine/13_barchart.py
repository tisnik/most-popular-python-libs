from plotnine.data import mpg
from plotnine import ggplot, aes, geom_bar

print(ggplot(mpg) + aes(x="cyl") + geom_bar())
