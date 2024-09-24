import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the box dimensions
x_min, x_max = 0, 2
y_min, y_max = 0, 4
z_min, z_max = 0, 2

# Define the vertices of the box
box_vertices = np.array([
    [x_min, y_min, z_min],
    [x_max, y_min, z_min],
    [x_max, y_max, z_min],
    [x_min, y_max, z_min],
    [x_min, y_min, z_max],
    [x_max, y_min, z_max],
    [x_max, y_max, z_max],
    [x_min, y_max, z_max],
])

# Define the vectors from (0,0,0) as omega_i
omega_i = np.array([
    [-0.710669, -0.0624022, 1.0],
    [1.49655, -1.01845, 1.0],
    [1.16995, 2.70106, 1.0]
])

# Define the CM point and the vectors from CM as omega_{CM,i}
CM = np.array([221/185, 90/37, 1])
omega_CM_i = np.array([
    [11.0584, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [-0.0904292, 1.0, 0.0]
])

# Plot the box and vectors
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the edges of the box
for edge in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]:
    ax.plot([box_vertices[edge[0], 0], box_vertices[edge[1], 0]],
            [box_vertices[edge[0], 1], box_vertices[edge[1], 1]],
            [box_vertices[edge[0], 2], box_vertices[edge[1], 2]], 'k-', lw=1.5)

# Plot omega_i vectors from the origin
for i, vector in enumerate(omega_i):
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b', arrow_length_ratio=0.1, linewidth=1.5)
    ax.text(vector[0], vector[1], vector[2], f'ω_{i+1}', color='blue', fontsize=12)

# Plot omega_CM_i vectors from the CM point
for i, vector in enumerate(omega_CM_i):
    ax.quiver(CM[0], CM[1], CM[2], vector[0], vector[1], vector[2], color='r', arrow_length_ratio=0.1, linewidth=1.5)
    ax.text(CM[0] + vector[0], CM[1] + vector[1], CM[2] + vector[2], f'ω_CM,{i+1}', color='red', fontsize=12)

# Plot the CM point
ax.scatter(CM[0], CM[1], CM[2], color='g', s=50, label='Center of Mass (CM)')
ax.text(CM[0], CM[1], CM[2], 'CM', color='green', fontsize=12)

# Scientific plot settings
ax.set_xlabel('X Axis', fontsize=14, labelpad=10)
ax.set_ylabel('Y Axis', fontsize=14, labelpad=10)
ax.set_zlabel('Z Axis', fontsize=14, labelpad=10)
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_zlim([z_min, z_max])

# Add grid, view angle, and legend
ax.grid(True)
ax.view_init(elev=20, azim=30)  # Set the view angle for better perspective
ax.legend(loc='upper left', fontsize=12)

plt.title('3D Box with Vectors ω and ω_CM', fontsize=16)
plt.tight_layout()
plt.show()
