import glfw

if not glfw.init():
    exit()

glfw.window_hint(glfw.RESIZABLE, glfw.FALSE) # Jendela tidak dapat diubah ukurannya
window = glfw.create_window(640, 480, "Petunjuk Jendela", None, None)

if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()