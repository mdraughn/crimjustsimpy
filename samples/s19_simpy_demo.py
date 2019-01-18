import timeit

import simpy


def calendar(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)

start = timeit.default_timer()
env = simpy.Environment()
env.process(calendar(env, 'court cycle', 1))
env.run(until=10)
end = timeit.default_timer()
print("Simulation took {0} seconds".format(end-start))
