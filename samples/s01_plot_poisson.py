from crimjustsimpy import Visualization
import crimjustsimpy.rangen as rg

num_points = 10000
p = rg.PoissonBounded(loc=2,mean=100)
data = [p() for i in range(num_points)]
Visualization.plot_hist(data, title="Poisson Distribution Sample",bins='ints')
