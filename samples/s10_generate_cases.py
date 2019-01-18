from typing import List, Any

import crimjustsim as cj
from crimjustsim import Visualization

max_cases = 100000

cf = cj.CaseFactory(convict_gen=cj.RandomScaledBetaProb(shape=5.0))

cases: List[cj.Case] = [next(cf) for i in range(max_cases)]
odds = [c.prob_convict for c in cases]
print("Generated {0} cases".format(len(cases)))
Visualization.plot_hist(odds, title="Case p(conviction)")
