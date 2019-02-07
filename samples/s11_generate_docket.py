from typing import List, Any

import crimjustsimpy as cj
from crimjustsimpy import Visualization, Docket

max_cases = 10000

cf = cj.CaseFactory(convict_gen=cj.RandomScaledBetaProb(shape=5.0))
d = Docket()
d.fill(max_cases,cf)
Visualization.plot_hist([c.prob_convict for c in d.cases], title="Case p(conviction)")
