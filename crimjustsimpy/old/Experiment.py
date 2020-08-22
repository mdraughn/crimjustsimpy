import timeit
import typing as typ
import pandas as pd

from crimjustsimpy.old import Docket, SimData, PleaBargainingStrategy, Trial


class Experiment:

    def __init__(self, *, docket_factory:typ.Iterator[Docket], trial: Trial,
                 plea_bargaining: PleaBargainingStrategy):

        # Store engine components.
        self.docket_factory = docket_factory
        self.trial = trial
        self.plea_bargaining = plea_bargaining

        # Data for the engine.
        self._data = SimData()

        self._run_time = 0.0

    @property
    def run_time(self):
        return self._run_time

    def run(self,iterations:int):
        start = timeit.default_timer()
        self._simulate(iterations)
        end = timeit.default_timer()

        self._run_time += end - start

    def to_cases_data_frame(self):
        cases = self._data.cases
        frame = pd.DataFrame({
            'id': [c.id for c in cases],
            'docketId': [c.docket.id for c in cases],
            'pConvict': [c.prob_convict for c in cases],
            'maxSentence': [c.sentence_if_convicted for c in cases],
            'plead': [c.plead for c in cases],
            'tried': [c.tried for c in cases],
            'acquitted': [c.acquitted for c in cases],
            'convicted': [c.convicted for c in cases],
            'guilty': [c.guilty for c in cases],
            'sentence': [c.sentence for c in cases],
        },index=[[c.docket.id for c in cases],[c.id for c in cases]])
        frame.index.names = ['docket', 'case']
        return frame

    def _simulate(self, iterations):
        for i in range(iterations):
            self._simulate_docket()

    def _simulate_docket(self):

        # Create the docket.
        docket = next(self.docket_factory)
        self._data.dockets.append(docket)

        # Plea bargaining phase.
        self.plea_bargaining.bargain(docket)

        # Trials for remaining cases.
        for case in docket.cases:
            if not case.plead:
                self.trial.try_case(case)
