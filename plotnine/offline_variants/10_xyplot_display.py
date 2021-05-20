from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

g = (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
     + geom_point()
     + stat_smooth(method='lm'))

g.save("10.png")
