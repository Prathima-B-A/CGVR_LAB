
import numpy as np
import matplotlib.pyplot as plt

# Original triangle using homogeneous coordinates
P = np.array([
    [1, 1, 1],
    [4, 1, 1],
    [2, 3, 1]
]).T

# Translation matrix
T = np.array([
    [1, 0, 2],
    [0, 1, 2],
    [0, 0, 1]
])

# Scaling matrix
S = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
])

# Rotation matrix (45 degrees)
theta = np.radians(45)
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Composite transformation: Translation, Rotation, Scaling
C = T @ R @ S

# Apply composite transformation
Q = C @ P

# Plot original triangle
plt.plot(
    list(P[0]) + [P[0][0]],
    list(P[1]) + [P[1][0]],
    'b-o', label="Original Triangle"
)

# Plot transformed triangle
plt.plot(
    list(Q[0]) + [Q[0][0]],
    list(Q[1]) + [Q[1][0]],
    'r-o', label="Composite Transformation"
)

plt.title("2D Composite Transformations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

print("Composite Transformation Matrix:")
print(C)

print("\nTransformed Coordinates:")
print(Q[:2].T)
