
import numpy as np
import matplotlib.pyplot as plt

# Original triangle
P = np.array([[1, 1, 1],
              [4, 1, 1],
              [2, 4, 1]]).T

# Scaling factors
sx = 2
sy = 2

# Scaling matrix
S = np.array([[sx, 0, 0],
              [0, sy, 0],
              [0, 0, 1]])

# Apply scaling
Q = S @ P

plt.plot([1, 4, 2, 1], [1, 1, 4, 1], 'b-o', label="Original")
plt.plot(list(Q[0]) + [Q[0][0]],
         list(Q[1]) + [Q[1][0]], 'r-o', label="Scaled")

plt.title("2D Scaling")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
