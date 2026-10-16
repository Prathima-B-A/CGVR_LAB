
import matplotlib.pyplot as plt

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Clipping window
xmin, ymin = 2, 2
xmax, ymax = 8, 8

# Calculate region code for a point
def compute_code(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Cohen-Sutherland line clipping algorithm
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        # Both endpoints are inside
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2

        # Both endpoints are outside in a common region
        if code1 & code2:
            return None

        # Select an endpoint outside the window
        code_out = code1 if code1 != 0 else code2

        # Find intersection with clipping boundary
        if code_out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax

        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin

        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax

        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        # Replace the outside endpoint
        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = compute_code(x2, y2)


# Original line endpoints
x1, y1 = 1, 5
x2, y2 = 9, 7

# Perform clipping
result = cohen_sutherland(x1, y1, x2, y2)

# Draw clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin],
         'k-', label="Clipping Window")

# Draw original line
plt.plot([x1, x2], [y1, y2], 'b--',
         label="Original Line")

# Draw clipped line if accepted
if result:
    cx1, cy1, cx2, cy2 = result
    plt.plot([cx1, cx2], [cy1, cy2], 'r-', linewidth=3,
             label="Clipped Line")
    print("Line accepted.")
    print("Clipped endpoints:", (cx1, cy1), (cx2, cy2))
else:
    print("Line rejected. It lies outside the clipping window.")

plt.title("Cohen-Sutherland Line Clipping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
