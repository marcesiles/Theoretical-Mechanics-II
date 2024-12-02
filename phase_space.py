import numpy as np
import matplotlib.pyplot as plt

# theoretical mechanics ii, hw3.
# phase space after a canonical transformation for a 
# 2-dimensional simple harmonic oscillator

# px vs x plots
# constants (adjust as needed)

X_0 = 1.0  # m
omega = 1.0  # rad/s
phi = 0.0  # rad, this is the phase constant
m = 1.0  # kg
lambda_ = 0

# time range
t = np.linspace(0, 50, 500)

# functions for x and px
x = X_0 * np.cos(omega * t - phi) * np.cos(lambda_)
px = - X_0 * m * omega * np.sin(omega * t - phi) * np.cos(lambda_)

# phase space plots 
plt.figure(figsize=(7, 5))
plt.plot(x, px, label='Phase space for the $x$ coordinate', color=(0.5, 0.4, 0.7))
plt.xlabel('$x(t)$')
plt.ylabel('$p_x(t)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.show()

# py vs y plots

lambda_ = 2 * np.pi

# functions for x and px
y = - X_0 * np.sin(omega * t - phi) * np.sin(lambda_)
py = - X_0 * m * omega * np.cos(omega * t - phi) * np.sin(lambda_)

# phase space plots 
plt.figure(figsize=(7, 5))
plt.plot(y, py, label='Phase space for the $y$ coordinate', color=(0.8, 0.2, 0.3))
plt.xlabel('$y(t)$')
plt.ylabel('$p_y(t)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.show()
