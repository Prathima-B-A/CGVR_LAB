
import glfw
import numpy as np
from OpenGL.GL import *

# Vertex shader
vertex_shader = """
#version 330 core
layout (location = 0) in vec3 aPos;
void main()
{
    gl_Position = vec4(aPos, 1.0);
}
"""

# Fragment shader
fragment_shader = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(1.0, 0.3, 0.2, 1.0);
}
"""

# Compile shader
def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        raise RuntimeError("Shader compilation failed: " + error)

    return shader

# Initialize GLFW
if not glfw.init():
    raise RuntimeError("Failed to initialize GLFW")

# Request OpenGL 3.3 core profile
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(
    glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE
)

window = glfw.create_window(
    800, 600, "OpenGL Shader Triangle", None, None
)

if not window:
    glfw.terminate()
    raise RuntimeError("Failed to create window")

glfw.make_context_current(window)

try:
    # Compile vertex and fragment shaders
    vs = compile_shader(vertex_shader, GL_VERTEX_SHADER)
    fs = compile_shader(fragment_shader, GL_FRAGMENT_SHADER)

    # Link shaders into a program
    program = glCreateProgram()
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)

    if not glGetProgramiv(program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(program).decode()
        raise RuntimeError("Program linking failed: " + error)

    glDeleteShader(vs)
    glDeleteShader(fs)

    # Triangle vertex coordinates
    vertices = np.array([
        -0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
         0.0,  0.5, 0.0
    ], dtype=np.float32)

    # Create VAO and VBO
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(
        GL_ARRAY_BUFFER, vertices.nbytes,
        vertices, GL_STATIC_DRAW
    )

    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE,
        3 * vertices.itemsize, ctypes.c_void_p(0)
    )
    glEnableVertexAttribArray(0)

    # Render loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

finally:
    if glfw.get_current_context():
        if 'VAO' in locals():
            glDeleteVertexArrays(1, [VAO])
        if 'VBO' in locals():
            glDeleteBuffers(1, [VBO])
        if 'program' in locals():
            glDeleteProgram(program)

    glfw.terminate()
