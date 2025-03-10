import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela, VBO, VAO, shader) ...

offsets = [(-0.5, -0.5), (0.5, -0.5), (0.0, 0.5)]

instanceVBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, instanceVBO)
glBufferData(GL_ARRAY_BUFFER, len(offsets) * 8, (GLfloat * len(offsets) * 2)(*sum(offsets, ())), GL_STATIC_DRAW)

# ... (pengaturan vertex attribute untuk instancing) ...

glDrawArraysInstanced(GL_TRIANGLES, 0, 3, 3) # Menggambar 3 instance

# ... (loop utama) ...