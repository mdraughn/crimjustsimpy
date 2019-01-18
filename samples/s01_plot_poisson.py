from crimjustsim import Visualization, RandomPoissonBounded

num_points = 10000
p = RandomPoissonBounded(loc=1,mean=4)
data = [next(p) for i in range(num_points)]
Visualization.plot_hist(data, title="Poisson Distribution Sample")
