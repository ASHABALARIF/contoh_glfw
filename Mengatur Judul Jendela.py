import glfw

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Judul Awal", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_window_title(window, "Judul Baru") # Mengatur judul jendela

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()