import cupy as np
import matplotlib.pyplot as plt

v = 1
res = (128, 128)
ds = 1e-1
dt = 1e-4
velocities = np.zeros((*res, 2))
velocities[res[0]//2 - 1:res[0]//2 + 1, :] = np.array([1, 0])


def divergence(matrix):
    dxp1 = np.roll(matrix, 1, axis=0)
    dxm1 = np.roll(matrix, -1, axis=0)
    dyp1 = np.roll(matrix, 1, axis=1)
    dym1 = np.roll(matrix, -1, axis=1)
    dmdx = (dxp1-dxm1)/(2 * ds)
    dmdy = (dyp1-dym1)/(2 * ds)
    return dmdx[:, :, 0] + dmdy[:, :, 1]


def laplacian(matrix):
    dxp1 = np.roll(matrix, 1, axis=0)
    dxm1 = np.roll(matrix, -1, axis=0)
    dyp1 = np.roll(matrix, 1, axis=1)
    dym1 = np.roll(matrix, -1, axis=1)
    dm2dx2 = (dxp1 - 2 * matrix + dxm1)/(2 * ds)
    dm2dy2 = (dyp1 - 2 * matrix + dym1)/(2 * ds)
    return dm2dx2[:, :, 0] + dm2dy2[:, :, 1]


def convective(matrix):
    dxp1 = np.roll(matrix, 1, axis=0)
    dxm1 = np.roll(matrix, -1, axis=0)
    dyp1 = np.roll(matrix, 1, axis=1)
    dym1 = np.roll(matrix, -1, axis=1)
    dmdx = (dxp1-dxm1)/(2 * ds)
    dmdy = (dyp1-dym1)/(2 * ds)
    return dmdx*matrix[:, :, :-1] + dmdy*matrix[:, :, 1:]


def gradient(matrix):
    

def pressure(velocities):
    return -1/2 * np.einsum("ijk,ijk->ij", velocities, velocities)


def pressure_grad(pressure):
    return np.stack(np.gradient(pressure, edge_order=2), -1)


# plt.imshow(np.linalg.norm(velocities, axis=-1), cmap="prism")
# plt.show()
t = 0
for i in range(200):
    print(i)
    t += dt
    velocities += (v*np.repeat(np.expand_dims(laplacian(velocities), -1), 2, -1) - convective(velocities) - pressure_grad(pressure(velocities)))*dt

plt.imshow(np.asnumpy(np.linalg.norm(velocities, axis=-1)), cmap="prism")
plt.show()
