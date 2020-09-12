from cProfile import Profile
from pstats import Stats
from crimjustsimpy.models.simple import SimpleRandomCase, SimpleRandomTrialEngine
from crimjustsimpy.trial import GenResults

def test():
    # print("Running trial...")
    case = SimpleRandomCase(cid=1, prob_convict=0.5, sentence_range=(5, 10))
    engine = SimpleRandomTrialEngine()

    for result in GenResults(engine, case,100000):
        # print(f"Trial result: {result.verdict} {result.sentence}")
        pass
    # print("Done..")


profiler = Profile()
profiler.runcall(test)
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
