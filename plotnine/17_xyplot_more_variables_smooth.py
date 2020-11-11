from plotnine.data import mpg
from plotnine import ggplot, aes, facet_grid, labs, geom_point, stat_smooth

print(ggplot(mpg)
      + facet_grid(facets="year~class")
      + aes(x="displ", y="hwy")
      + labs(
          x="Engine Size",
          y="Miles per Gallon",
          title="Miles per Gallon for Each Year and Vehicle Class")
      + geom_point()
      + stat_smooth(method='lm'))
