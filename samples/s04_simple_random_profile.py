from cProfile import Profile
from pstats import Stats
from crimjustsimpy.models.simple import SimpleRandomCase, SimpleRandomTrialEngine
from crimjustsimpy.trial import GenResults, SummarizeResults, ResultSummary

case = SimpleRandomCase(cid=1, prob_convict=0.5, sentence_range=(5, 10))
engine = SimpleRandomTrialEngine()

profiler = Profile()
summary:ResultSummary = profiler.runcall(lambda: SummarizeResults(engine, case, 10000))
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
print(f"guilty %= {100.0 * float(summary.guilty_count) / float(summary.count)}, mean_sentence = {float(summary.sentence_sum) / float(summary.guilty_count)}")
