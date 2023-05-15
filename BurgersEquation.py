import numpy as np

def burgers(u, t):
    nu = 0.1
    dx = L / (nx - 1)
    dt = nu * dx**2
    u_next = u.copy()
    u_next[1:-1] = u[1:-1] - u[1:-1] * (dt / dx) * (u[1:-1] - u[:-2]) + nu * (dt / dx**2) * (u[2:] - 2 * u[1:-1] + u[:-2])
    u_next[0] = u[0] - u[0] * (dt / dx) * (u[0] - u[-2]) + nu * (dt / dx**2) * (u[1] - 2 * u[0] + u[-2])
    u_next[-1] = u[0] - u[-1] * (dt / dx) * (u[-1] - u[-2]) + nu * (dt / dx**2) * (u[0] - 2 * u[-1] + u[-2])
    return u_next

L = 2.0
nx= 81
nt= 100
dx= L / (nx - 1)
u = np.zeros((nx, 1))
x = np.linspace(0, L, nx)
u_init = np.exp(-((x - 0.5) / 0.1)**2)
u = u_init.reshape(nx, 1)

dt = 0.01
for n in range(nt):
    k1 = dt * burgers(u, n * dt)
    k2 = dt * burgers(u + 0.5 * k1, n * dt + 0.5 * dt)
    k3 = dt * burgers(u + 0.5 * k2, n * dt + 0.5 * dt)
    k4 = dt * burgers(u + k3, (n + 1) * dt)
    u += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)