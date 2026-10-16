import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math


# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW initialization failed")

# Create window
window = glfw.create_window(800, 600, "Bouncing Ball - CGVR", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window creation failed")

glfw.make_context_current(window)

# Set background color
glClearColor(0.1, 0.1, 0.1, 1.0)

# Set 2D projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-10, 10, -7.5, 7.5)

glMatrixMode(GL_MODELVIEW)


# Ball properties
x = 0.0
y = 5.0
radius = 1.0

velocity_y = 0.0
gravity = -9.8

# Ground level
ground = -5.5


def draw_circle(x, y, radius):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)

    for i in range(101):
        angle = 2 * math.pi * i / 100
        glVertex2f(
            x + radius * math.cos(angle),
            y + radius * math.sin(angle)
        )

    glEnd()


# Main loop
last_time = glfw.get_time()

while not glfw.window_should_close(window):

    current_time = glfw.get_time()
    delta_time = current_time - last_time
    last_time = current_time

    # Apply gravity
    velocity_y += gravity * delta_time
    y += velocity_y * delta_time

    # Bounce when ball hits ground
    if y - radius <= ground:
        y = ground + radius
        velocity_y = 8.0

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw ground
    glColor3f(0.2, 0.8, 0.2)

    glBegin(GL_QUADS)
    glVertex2f(-10, ground)
    glVertex2f(10, ground)
    glVertex2f(10, ground - 0.5)
    glVertex2f(-10, ground - 0.5)
    glEnd()

    # Draw ball
    glColor3f(1.0, 0.2, 0.2)
    draw_circle(x, y, radius)

    # Display
    glfw.swap_buffers(window)
    glfw.poll_events()


# Close GLFW
glfw.terminate()