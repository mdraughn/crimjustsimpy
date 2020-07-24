from crimjustsimpy import Visualization
from crimjustsimpy.random import RandomScaledBetaProb

num_points = 10000
p = RandomScaledBetaProb()
data = [next(p) for i in range(num_points)]
Visualization.plot_hist(data, title="Beta Distribution Sample")
