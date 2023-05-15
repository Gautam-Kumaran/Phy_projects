# Added to Github

from numpy import *
from matplotlib.pyplot import *
from matplotlib.animation import FuncAnimation

def van_der_pol(t, y, mu):
    y1, y2 = y
    return [y2, mu*(1-y1**2)*y2 - y1]

def graph(mu):
    y0 = [0.5, 0.5]
    t0, tmax, dt = 0, 1000, 0.1
    mu = mu
    t = arange(t0, tmax, dt)
    n = len(t)
    y = zeros((n, len(y0)))
    y[0, 0:n] = y0

    for i in range(n-1):
        k1 = dt * array(van_der_pol(t[i]        ,y[i, 0:n]        ,mu))
        k2 = dt * array(van_der_pol(t[i] + dt/2 ,y[i, 0:n] + k1/2 ,mu))
        k3 = dt * array(van_der_pol(t[i] + dt/2 ,y[i, 0:n] + k2/2 ,mu))
        k4 = dt * array(van_der_pol(t[i] + dt   ,y[i, 0:n] + k3   ,mu))
        y[i+1, 0:n] = y[i, 0:n] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return(y[0:n, 0], y[0:n, 1])

fig, ax = subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlabel('Position')
ax.set_ylabel('Speed')
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

def init():
    line.set_data([], [])
    return line,

def animate(mu):
    y1, y2 = graph(mu)
    line.set_data(y1, y2)
    return line,

anim = FuncAnimation(fig, animate, frames=arange(0.01, 3.0, 0.1), init_func=init, interval=0.5, blit=True)
show()