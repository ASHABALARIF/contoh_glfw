import glfw

if not glfw.init():
    exit()

monitor = glfw.get_primary_monitor()
mode = glfw.get_video_mode(monitor)
window = glfw.create_window(mode.size.width, mode.size.height, "Layar Penuh", monitor, None)

if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()