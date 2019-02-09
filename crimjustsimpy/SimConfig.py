import timeit
import typing as typ
import pandas as pd
import simpy

from crimjustsimpy import Trial, PleaBargainingStrategy, SimData, Docket


class SimConfig:

    def __init__(self, *,
                 docket_factory:typ.Iterator[Docket],
                 trial:Trial,
                 plea_bargaining:PleaBargainingStrategy,
                 docket_interval:int = 1,
                 plea_wait:int = 0,
                 trial_wait:int = 0,
                 active_period:int = 1):

        # Store engine components.
        self.docket_factory = docket_factory
        self.trial = trial
        self.plea_bargaining = plea_bargaining

        # Config info hardcoded for now.
        self.docket_interval = docket_interval
        self.plea_wait = plea_wait
        self.trial_wait = trial_wait
        self.active_period = active_period
