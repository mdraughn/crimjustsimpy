from cProfile import Profile
from pstats import Stats
from crimjustsimpy.models.simple import SimpleRandomCase, SimpleRandomTrialEngine
from crimjustsimpy.trial import GenResults, SummarizeResults, ResultSummary, TrialEstimatorBase, CachingTrialEstimator

def test():
    engine = SimpleRandomTrialEngine()
    estimator = CachingTrialEstimator(TrialEstimatorBase(engine, 1000000))

    case = SimpleRandomCase(cid=1, prob_convict=0.5, sentence_range=(5, 10))
    result = estimator.estimate(case)
    result = estimator.estimate(case)
    result = estimator.estimate(case)
    result = estimator.estimate(case)
    return result

profiler = Profile()
summary:ResultSummary = profiler.runcall(test)
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
print(f"guilty %= {100.0 * float(summary.guilty_count) / float(summary.count)}, mean_sentence = {float(summary.sentence_sum) / float(summary.guilty_count)}")
