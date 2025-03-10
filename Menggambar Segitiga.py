import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, vertices)
glEnableVertexAttribArray(0)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3) # Menggambar segitiga
    glfw.swap_buffers(window)
    glfw.poll_events()

# ... (kode terminasi) ...