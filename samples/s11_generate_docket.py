import crimjustsimpy as cj
from crimjustsimpy import Visualization
from crimjustsimpy.old import Docket
from crimjustsimpy.random import RandomScaledBetaProb

max_cases = 10000

cf = cj.CaseFactory(convict_gen=RandomScaledBetaProb(shape=5.0))
d = Docket()
d.fill(max_cases,cf)
Visualization.plot_hist([c.prob_convict for c in d.cases], title="Case p(conviction)")
