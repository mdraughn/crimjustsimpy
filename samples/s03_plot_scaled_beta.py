from crimjustsimpy import Visualization
import crimjustsimpy.rangen as rg

num_points = 10000
p = rg.ScaledBetaProb()
data = [p() for i in range(num_points)]
Visualization.plot_hist(data, title="Beta Distribution Sample")
