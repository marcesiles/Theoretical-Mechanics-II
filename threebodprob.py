import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sqrt, solve, diff, lambdify
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 1
M1 = 10.0
M2 = 20.0
m = 0.25
r21 = 1
alpha1 = M2 / (M1 + M2)
alpha2 = -M1 / (M1 + M2)
xlim = 1
ylim = 1

# Symbols
alpha, beta = symbols('alpha beta')

# Effective potential Ueff
Ueff = (G * (M1 + M2) * m / r21) * (alpha2 / sqrt((alpha - alpha1)**2 + beta**2)
                                     - alpha1 / sqrt((alpha - alpha2)**2 + beta**2)
                                     - 0.5 * (alpha**2 + beta**2))

# Derivatives (Partial derivatives of Ueff)
dUeff_alpha = diff(Ueff, alpha)
dUeff_beta = diff(Ueff, beta)

# Solve for Lagrange points
solutions = solve([dUeff_alpha, dUeff_beta], (alpha, beta))
lagrange_points = [(sol[0].evalf(), sol[1].evalf()) for sol in solutions]
print("Lagrange Points:", lagrange_points)

# Convert symbolic function to numerical functions
Ueff_func = lambdify([alpha, beta], Ueff, 'numpy')

# Create grid for contour and 3D plotting
alpha_vals = np.linspace(-xlim - 0.5, xlim + 0.5, 400)
beta_vals = np.linspace(-ylim - 0.5, ylim + 0.5, 400)
alpha_grid, beta_grid = np.meshgrid(alpha_vals, beta_vals)
Ueff_values = Ueff_func(alpha_grid, beta_grid)

# 3D plot of Ueff with purple color map
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(alpha_grid, beta_grid, Ueff_values, cmap='Purples')  # Changed to purple color map
ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('Ueff(alpha, beta)')
plt.show()

# Contour plot of Ueff with Lagrange points using arbitrary color map
fig, ax = plt.subplots(figsize=(10, 7))
contour_levels = np.linspace(-16, -10.5, 12)
contour = ax.contour(alpha_grid, beta_grid, Ueff_values, levels=contour_levels, cmap='plasma')  # Arbitrary color map
ax.clabel(contour, inline=True, fontsize=8)
ax.set_xlabel('alpha')
ax.set_ylabel('beta')

# Plot Lagrange points
for i, point in enumerate(lagrange_points):
    ax.plot(point[0], point[1], 'ro')
    ax.text(point[0], point[1], f"L{i+1}", color='red')

# Mark masses M1 and M2
ax.plot(alpha1, 0, 'bo', markersize=10)
ax.text(alpha1, 0, 'M1', color='blue')
ax.plot(alpha2, 0, 'bo', markersize=15)
ax.text(alpha2, 0, 'M2', color='blue')

plt.show()