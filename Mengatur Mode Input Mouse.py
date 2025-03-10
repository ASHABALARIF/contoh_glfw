import glfw

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Mode Input Mouse", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED) # Menyembunyikan kursor

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()