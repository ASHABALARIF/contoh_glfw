import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, (GLfloat * len(vertices))(*vertices), GL_STATIC_DRAW)

# ... (pengaturan vertex attribute) ...

# ... (loop utama) ...