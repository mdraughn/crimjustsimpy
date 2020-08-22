import crimjustsimpy as cj
from crimjustsimpy import Visualization

# Setup parameters for the experiment.
from crimjustsimpy.rangen import RandomScaledBetaProb, RandomPoissonBounded

AVG_CASES_PER_INTERVAL = 100
MAX_CASES_PER_INTERVAL = 300
MIN_PROB_CONVICT = 0.05
MEAN_PROB_CONVICT = 0.4
MAX_PROB_CONVICT = 0.95
PROB_PLEA=0.8
ITERATIONS = 20 * 365

# Configure the case factory.
convict_gen = RandomScaledBetaProb(shape=10.0,
    lower=MIN_PROB_CONVICT,middle=MEAN_PROB_CONVICT,upper=MAX_PROB_CONVICT)
case_factory = cj.CaseFactory(convict_gen=convict_gen)

# Configure the docket factory.
arrival_gen = RandomPoissonBounded(mean=AVG_CASES_PER_INTERVAL, upper=MAX_CASES_PER_INTERVAL)
docket_factory = cj.DocketFactory(case_factory=case_factory, arrival_gen=arrival_gen)

# Configure the plea bargaining logic.
plea_bargaining = cj.PleaBargainingAtRandom(prob_plea=PROB_PLEA)

# Configure the trial logic.
trial = cj.Trial()

# Configure the experiment.
config = cj.SimConfig(docket_factory=docket_factory, trial=trial, plea_bargaining=plea_bargaining,
                      docket_interval= 30, plea_wait = 60, trial_wait = 90, active_period=ITERATIONS)
engine = cj.SimEngine(config)

# Run it.
engine.run()
print("Simulation ran for {0} seconds.".format(engine.run_time))
df = engine.to_cases_data_frame()

# Plot docket sizes histogram.
Visualization.plot_docket_sizes_hist(df)

# Plot case probability of conviction histogram.
Visualization.plot_prob_guilt_hist(df)

# Pie chart of pleas vs trials.
Visualization.plot_pleas_vs_trials_pie(df)

# Pie chart of trial results.
Visualization.plot_trial_results_pie(df)

# Pie chart of guilty/not guilty.
Visualization.plot_guilt_summary_pie(df)

# Pie chart of case results.
Visualization.plot_case_results_pie(df)

# Plot sentencing histogram.
Visualization.plot_sentences_hist(df)
