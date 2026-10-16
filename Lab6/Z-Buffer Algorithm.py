
import numpy as np
import matplotlib.pyplot as plt

# Screen size
width = 200
height = 200

# Initialize Z-buffer with infinity
zbuffer = np.full((height, width), np.inf)

# Initialize image buffer
image = np.zeros((height, width, 3))

# Define two overlapping triangles
triangles = [
    {
        "vertices": [(30, 30, 0.3), (170, 30, 0.3),
                     (100, 170, 0.3)],
        "color": [1, 0, 0]
    },
    {
        "vertices": [(50, 60, 0.6), (180, 60, 0.6),
                     (100, 190, 0.6)],
        "color": [0, 1, 0]
    }
]

# Calculate the area of a triangle
def edge(a, b, x, y):
    return ((x - a[0]) * (b[1] - a[1])
            - (y - a[1]) * (b[0] - a[0]))

# Apply Z-buffer algorithm
for triangle in triangles:
    vertices = triangle["vertices"]
    color = triangle["color"]

    v0, v1, v2 = vertices

    # Bounding box
    xmin = max(0, int(min(v0[0], v1[0], v2[0])))
    xmax = min(width - 1, int(max(v0[0], v1[0], v2[0])))
    ymin = max(0, int(min(v0[1], v1[1], v2[1])))
    ymax = min(height - 1, int(max(v0[1], v1[1], v2[1])))

    area = edge(v0, v1, v2[0], v2[1])

    if area == 0:
        continue

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):

            # Barycentric coordinates
            w0 = edge(v1, v2, x, y) / area
            w1 = edge(v2, v0, x, y) / area
            w2 = edge(v0, v1, x, y) / area

            # Check whether pixel is inside triangle
            if w0 >= 0 and w1 >= 0 and w2 >= 0:
                # Interpolate depth
                z = (w0 * v0[2] +
                     w1 * v1[2] +
                     w2 * v2[2])

                # Smaller z means closer to viewer
                if z < zbuffer[y, x]:
                    zbuffer[y, x] = z
                    image[y, x] = color

# Display final image
plt.figure(figsize=(7, 6))
plt.imshow(image, origin="lower", extent=[0, width, 0, height])
plt.title("Z-Buffer Algorithm")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()

print("Z-Buffer algorithm executed successfully.")
