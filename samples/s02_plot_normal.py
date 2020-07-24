from crimjustsimpy import Visualization
from crimjustsimpy.random import RandomNormalBounded

num_points = 10000
p = RandomNormalBounded(lower=-10,upper=10)
data = [next(p) for i in range(num_points)]
Visualization.plot_hist(data, title="Normal Distribution Sample")
