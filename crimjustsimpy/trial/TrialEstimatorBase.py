from typing import Callable
from ..core import IdGenerator
from . import ITrialEstimator, ITrialEngine, ICase, ResultSummary, Verdict


class TrialEstimatorBase(ITrialEstimator):
    engine: ITrialEngine
    reps: int

    def __init__(self, engine: ITrialEngine, reps: int):
        assert isinstance(engine, ITrialEngine)
        assert reps is not None and reps > 0
        self.engine = engine
        self.reps = reps

    def estimate(self, case: ICase) -> ResultSummary:
        """Estimate the outcome of a case."""

        guilty_count = 0
        not_guilty_count = 0
        mistrial_count = 0
        count = 0
        sentence_sum = 0
        engine = self.engine

        for i in range(self.reps):
            result = engine.try_case(case)
            verdict = result.verdict
            sentence = result.sentence
            if verdict==Verdict.guilty:
                guilty_count += 1
            elif verdict==Verdict.not_guilty:
                not_guilty_count +=1
            else:
                mistrial_count +=1
            count += 1
            sentence_sum += sentence

        summary = ResultSummary()
        summary.guilty_count = guilty_count
        summary.not_guilty_count = not_guilty_count
        summary.mistrial_count = mistrial_count
        summary.count = count
        summary.sentence_sum =sentence_sum

        return summary