from cachetools import Cache, LFUCache

from crimjustsimpy.trial import ITrialEstimator, ICase, ResultSummary


class CachingTrialEstimator(ITrialEstimator):
    estimator: ITrialEstimator
    cache: Cache

    def __init__(self, estimator: ITrialEstimator):
        self.estimator = estimator
        self.cache = LFUCache(10000)

    def estimate(self, case: ICase) -> ResultSummary:
        key = f"{self.estimator.key}:{case.key}"
        if key not in self.cache:
            result = self.estimator.estimate(case)
            self.cache[key] = result
        else:
            result = self.cache[key]
        return result
