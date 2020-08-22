import timeit
import pandas as pd
import simpy

from crimjustsimpy.old import SimData, SimConfig


class SimEngine:

    def __init__(self, config: SimConfig, *, data: SimData = None):

        # Store engine components.
        self.config = config


        # Data for the engine.
        self.data = data or SimData()

        # Stats
        self._run_time = 0.0

        # Initialize the simulation.
        self.env = simpy.Environment()
        self.env.process(self._proc_caseload())

    @property
    def run_time(self):
        return self._run_time

    def run(self, iterations:int = None):
            start = timeit.default_timer()
            self.env.run(until=iterations)
            end = timeit.default_timer()
            self._run_time += end - start

    def _proc_caseload(self):
        while self.env.now < self.config.active_period:
            yield self.env.timeout(self.config.docket_interval)
            self.env.process(self._proc_docket())

    def _proc_docket(self):

        # Create the docket.
        docket = next(self.config.docket_factory)
        for case in docket.cases:
            case.time_created = self.env.now
        self.data.dockets.append(docket)
        yield self.env.timeout(self.config.plea_wait)

        # Plea bargaining phase.
        self.config.plea_bargaining.bargain(docket)
        for case in docket.cases:
            case.time_plead = self.env.now
        yield self.env.timeout(self.config.trial_wait)

        # Trials for remaining cases.
        for case in docket.cases:
            if not case.plead:
                self.config.trial.try_case(case)
                case.time_tried = self.env.now

    def to_cases_data_frame(self):
        cases = self.data.cases
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
