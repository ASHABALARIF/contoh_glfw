import glfw

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Ukuran Jendela", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_window_size(window, 800, 600) # Mengatur ukuran jendela

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()