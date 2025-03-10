import glfw
from OpenGL.GL import *
import numpy as np

# ... (kode inisialisasi jendela dan shader) ...

transform = glGetUniformLocation(shader_program, "transform")
matrix = np.identity(4, dtype=np.float32) # Matriks identitas
glUniformMatrix4fv(transform, 1, GL_FALSE, matrix)

# ... (loop utama) ...