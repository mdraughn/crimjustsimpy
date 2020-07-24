from typing import List, Any
import crimjustsimpy as cj
from crimjustsimpy.random import RandomScaledBetaProb
from crimjustsimpy import Visualization

max_cases = 100000

cf = cj.CaseFactory(convict_gen=RandomScaledBetaProb(shape=5.0))

cases: List[cj.Case] = [next(cf) for i in range(max_cases)]
odds = [c.prob_convict for c in cases]
print("Generated {0} cases".format(len(cases)))
Visualization.plot_hist(odds, title="Case p(conviction)")
