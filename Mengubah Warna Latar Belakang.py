import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

glClearColor(0.2, 0.3, 0.3, 1.0) # Mengatur warna latar belakang

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT) # Membersihkan layar dengan warna latar belakang
    glfw.swap_buffers(window)
    glfw.poll_events()

# ... (kode terminasi) ...