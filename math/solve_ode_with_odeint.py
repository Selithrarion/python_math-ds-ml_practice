import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# 1.
# hello world
#
# def model(y, t, k):
#     dydt = -k * y
#     return dydt
#
#
# # initial condition
# y0 = 5
# # how many time points
#
# t = np.linspace(0, 50)
#
# # solve ODE
# k = 0.1
# y1 = odeint(model, y0, t, args=(k,))
# k = 0.2
# y2 = odeint(model, y0, t, args=(k,))
# k = 0.5
# y3 = odeint(model, y0, t, args=(k,))
#
# # render
# plt.plot(t, y1, 'r-', linewidth=2, label='k=0.1')
# plt.plot(t, y2, 'b--', linewidth=2, label='k=0.2')
# plt.plot(t, y3, 'g:', linewidth=2, label='k=0.5')
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()


# 2.
# dy(t)/dt = -y(t) + 1
# y(0) = 0
#
# def model(y, t):
#     dydt = -y + 1.0
#     return dydt
#
#
# y0 = 0
# t = np.linspace(0, 5)
# y = odeint(model, y0, t)
#
# plt.plot(t, y)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()


# 3.
# 5*dt(y)/dt = -y(t) + u(t)
# y(0) = 1
# u steps from 0 to 2 at t=10
#
# def model(y, t):
#     if t < 10.0:
#         u = 0
#     else:
#         u = 2
#     dydt = (-y + u) / 5.0
#     return dydt
#
#
# y0 = 1
# t = np.linspace(0, 40)
# y = odeint(model, y0, t)
#
# plt.plot(t, y, 'r-', label='Output (y(t))')
# plt.plot([0, 10, 10, 40], [0, 0, 2, 2], 'b-', label='Input (u(t))')
# plt.ylabel('values')
# plt.xlabel('time')
# plt.legend(loc='best')
# plt.show()


# 4.
# dx(t)/dt = 3exp(-t)
# dy(t)/dt = 3 - y(t)
# x(0) = 0
# y(0) = 0
#
# def model(z, t):
#     dxdt = 3 * np.exp(-t)
#     dydt = -z[1] + 3
#     dzdt = [dxdt, dydt]
#     return dzdt
#
#
# z0 = [0, 0]
# t = np.linspace(0, 5)
# z = odeint(model, z0, t)
#
# plt.plot(t, z[:, 0], 'b-', label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
# plt.plot(t, z[:, 1], 'r--', label=r'$\frac{dy}{dt}=-y+3$')
# plt.ylabel('response')
# plt.xlabel('time')
# plt.legend(loc='best')
# plt.show()


# 5.
# 2*dx(t)/dt = -x(t) + u(t)
# 5*dy(t)/dt = -y(t) + x(t)
# u = 2S(t-5)
# x(0) = 0
# y(0) = 0
#
def model(z, t, u):
    x = z[0]
    y = z[1]
    dxdt = (-x + u) / 2
    dydt = (-y + x) / 5
    dzdt = [dxdt, dydt]
    return dzdt


# initial
z0 = [0, 0]
# time points number
n = 401
# time points
t = np.linspace(0, 40, n)

# step input
u = np.zeros(n)
# change to 2 at time 5
u[50:] = 2

# store
x = np.empty_like(t)
y = np.empty_like(t)
#  initial store
x[0] = z0[0]
y[0] = z0[1]

# solve ODE
for i in range(1, n):
    # span for next time step
    timespan = [t[i - 1], t[i]]
    # solve next step
    z = odeint(model, z0, timespan, args=(u[i],))
    # save to store
    x[i] = z[1][0]
    y[i] = z[1][1]
    # next
    z0 = z[1]

# render
plt.plot(t, u, 'g:', label='u(t)')
plt.plot(t, x, 'b-', label='x(t)')
plt.plot(t, y, 'r--', label='y(t)')
plt.ylabel('values')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
