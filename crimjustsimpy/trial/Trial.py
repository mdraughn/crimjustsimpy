from typing import Iterable

from crimjustsimpy.trial import ITrialEngine, ICase, IResult


def GenResults(trial_engine: ITrialEngine, case: ICase, n: int) -> Iterable[IResult]:
    return [trial_engine.try_case(case) for i in range(n)]
