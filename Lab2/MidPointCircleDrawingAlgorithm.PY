import matplotlib.pyplot as plt

# Take input from user
xc = int(input("Enter center x (xc): "))
yc = int(input("Enter center y (yc): "))
r = int(input("Enter radius (r): "))

# Initial values
x = 0
y = r
p = 1 - r

points_x = []
points_y = []

# Function to plot all 8 symmetric points
def plot_points(x, y):
    points_x.extend([
        xc + x, xc - x,
        xc + x, xc - x,
        xc + y, xc - y,
        xc + y, xc - y
    ])

    points_y.extend([
        yc + y, yc + y,
        yc - y, yc - y,
        yc + x, yc + x,
        yc - x, yc - x
    ])

# Midpoint Circle Algorithm
while x <= y:

    plot_points(x, y)

    if p < 0:
        # Choose East pixel
        p = p + 2 * x + 3
    else:
        # Choose South-East pixel
        p = p + 2 * (x - y) + 5
        y = y - 1

    x = x + 1

# Display points
print("\nPoints generated:")
for i in range(len(points_x)):
    print(f"({points_x[i]}, {points_y[i]})")

# Plot the circle
plt.scatter(points_x, points_y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint Circle Drawing Algorithm")
plt.grid(True)
plt.axis("equal")
plt.show()
