def car(env):
  while True:
    print('car Start parking at %d' % env.now)
    parking_duration = 5
    yield env.timeout(parking_duration)
    
    print('car Start driving at %d' % env.now)
    trip_duration = 2
    yield env.timeout(trip_duration)

def car1(env):
  while True:
    print('car1 Start parking at %d' % env.now)
    parking_duration = 3
    yield env.timeout(parking_duration)
    
    print('car1 Start driving at %d' % env.now)
    trip_duration = 4
    yield env.timeout(trip_duration)

import simpy
env = simpy.Environment()
env.process(car(env))
env.process(car1(env))
env.run(until=15)