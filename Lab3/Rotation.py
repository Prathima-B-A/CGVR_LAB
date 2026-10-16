
import numpy as np
import matplotlib.pyplot as plt

# Original triangle
P = np.array([[1, 1, 1],
              [4, 1, 1],
              [2, 4, 1]]).T

# Rotation angle
theta = np.radians(45)

# Rotation matrix
R = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta),  np.cos(theta), 0],
              [0, 0, 1]])

# Apply rotation
Q = R @ P

plt.plot([1, 4, 2, 1], [1, 1, 4, 1], 'b-o', label="Original")
plt.plot(list(Q[0]) + [Q[0][0]],
         list(Q[1]) + [Q[1][0]], 'r-o', label="Rotated")

plt.title("2D Rotation (45 degrees)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
