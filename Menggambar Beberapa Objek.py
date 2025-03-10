import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela, VBO, VAO, shader) ...

# Menggambar objek pertama
glBindVertexArray(VAO1)
glDrawArrays(GL_TRIANGLES, 0, 3)

# Menggambar objek kedua
glBindVertexArray(VAO2)
glDrawArrays(GL_TRIANGLES, 0, 3)

# ... (loop utama) ...