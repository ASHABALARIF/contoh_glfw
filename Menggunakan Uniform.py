import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela dan shader) ...

uniform_color = glGetUniformLocation(shader_program, "ourColor")
glUniform4f(uniform_color, 0.0, 1.0, 0.0, 1.0) # Mengatur nilai uniform

# ... (loop utama) ...