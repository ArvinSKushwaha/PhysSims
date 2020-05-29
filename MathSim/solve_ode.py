import matplotlib.pyplot as plt
import cupy as cp
import numpy as np


# Conditions: [[starting_position, starting_velocity]]
def verlet_integrator(acceleration, conditions, times, dt=1e-5):
    positions = conditions[:, 0]
    velocities = conditions[:, 1]
    for t in np.arange(times[0], times[1], step=dt):
        positions += velocities * dt/2.0
        velocities += acceleration(positions, velocities, t) * dt
        positions += velocities * dt/2.0
    return positions, velocities


def verlet_iterator(acceleration, conditions, times, dt=1e-5):
    positions = conditions[:, 0]
    velocities = conditions[:, 1]
    for t in np.arange(times[0], times[1], step=dt):
        positions += velocities * dt/2.0
        velocities += acceleration(positions, velocities, t) * dt
        positions += velocities * dt/2.0
        yield positions, velocities, t

def accel(positions, velocities, time):
    return np.array([time, 0])


initial = np.array([[[0., 0.],[10., 1.]]])
positions = []
t = []
for i, (pos, vel, time) in enumerate(verlet_iterator(accel, initial, (0, 10), dt=1e-5)):
    if(i % 10000 == 0):
        print(time)
    positions.append(pos.copy())
    t.append(time)

positions = np.array(positions)
print(positions.T.shape)
plt.plot(*positions.T[:,0,:])
plt.show()
