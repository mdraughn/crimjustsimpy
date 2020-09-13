from typing import Iterable

from crimjustsimpy.trial import ITrialEngine, ICase, IResult, ResultSummary, Verdict, CachingTrialEstimator
from crimjustsimpy.trial import TrialEstimatorBase


def GenResults(trial_engine: ITrialEngine, case: ICase, n: int) -> Iterable[IResult]:
    assert isinstance(trial_engine,ITrialEngine)
    assert isinstance(case,ICase)
    # for i in range(n):
    #     yield trial_engine.try_case(case)
    return (trial_engine.try_case(case) for i in range(n))

def SummarizeResults(trial_engine: ITrialEngine, case: ICase, n: int) -> ResultSummary:
    assert isinstance(trial_engine,ITrialEngine)
    assert isinstance(case,ICase)

    estimator = CachingTrialEstimator(TrialEstimatorBase(trial_engine, n))
    result = estimator.estimate(case)
    return result

def SummarizeResults_OLD(trial_engine: ITrialEngine, case: ICase, n: int) -> ResultSummary:
    assert isinstance(trial_engine,ITrialEngine)
    assert isinstance(case,ICase)

    guilty_count = 0
    not_guilty_count = 0
    mistrial_count = 0
    count = 0
    sentence_sum = 0

    for i in range(n):
        result = trial_engine.try_case(case)
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
