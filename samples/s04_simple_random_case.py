from crimjustsimpy.models.simple import SimpleRandomCase, SimpleRandomTrialEngine

print("Running trial...")
case = SimpleRandomCase(cid=1, prob_convict=0.5, sentence_range=(5, 10))
trial = SimpleRandomTrialEngine()
result = trial.try_case(case)
print(f"Trial result: {result.verdict} {result.sentence}")
