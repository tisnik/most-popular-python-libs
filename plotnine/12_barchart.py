from plotnine.data import mpg
from plotnine import ggplot, aes, geom_bar

print(ggplot(mpg) + aes(x="class") + geom_bar())
