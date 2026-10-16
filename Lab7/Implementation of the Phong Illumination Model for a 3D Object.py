
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Create a 3D sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))

# Surface normals of a unit sphere
normals = np.stack((x, y, z), axis=-1)

# Light and viewing directions
light = np.array([1, 1, 1], dtype=float)
light /= np.linalg.norm(light)

view = np.array([0, 0, 1], dtype=float)

# Phong model parameters
ka = 0.2       # Ambient coefficient
kd = 0.6       # Diffuse coefficient
ks = 0.5       # Specular coefficient
shininess = 30 # Shininess factor

# Ambient illumination
ambient = ka

# Diffuse illumination
diffuse = kd * np.maximum(
    np.sum(normals * light, axis=-1), 0
)

# Reflection vector R = 2(N.L)N - L
dot_nl = np.sum(normals * light, axis=-1)
reflection = 2 * dot_nl[..., None] * normals - light

# Specular illumination
specular = ks * np.maximum(
    np.sum(reflection * view, axis=-1), 0
) ** shininess

# Total Phong illumination
intensity = ambient + diffuse + specular
intensity = np.clip(intensity, 0, 1)

# Display the shaded sphere
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,
    facecolors=plt.cm.gray(intensity),
    linewidth=0,
    antialiased=True,
    shade=False
)

ax.set_title("Phong Illumination Model")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_box_aspect([1, 1, 1])

plt.show()

print("Phong illumination model implemented successfully.")
