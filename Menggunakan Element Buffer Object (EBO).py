import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

indices = [0, 1, 2]

EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * 4, (GLuint * len(indices))(*indices), GL_STATIC_DRAW)

# ... (loop utama) ...