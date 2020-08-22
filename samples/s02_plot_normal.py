from crimjustsimpy import Visualization
import crimjustsimpy.rangen as rg

num_points = 10000
p = rg.NormalBounded(lower=-10,upper=10)
data = [p() for i in range(num_points)]
Visualization.plot_hist(data, title="Normal Distribution Sample")
