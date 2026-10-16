
import numpy as np
import matplotlib.pyplot as plt

# Original triangle
P = np.array([[1, 1, 1],
              [4, 1, 1],
              [2, 4, 1]]).T

# Reflection matrix about X-axis
F = np.array([[1,  0, 0],
              [0, -1, 0],
              [0,  0, 1]])

# Apply reflection
Q = F @ P

plt.plot([1, 4, 2, 1], [1, 1, 4, 1], 'b-o', label="Original")
plt.plot(list(Q[0]) + [Q[0][0]],
         list(Q[1]) + [Q[1][0]], 'r-o', label="Reflected")

plt.title("2D Reflection about X-axis")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
