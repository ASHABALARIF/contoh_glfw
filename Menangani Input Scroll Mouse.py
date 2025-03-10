import glfw

def scroll_callback(window, xoffset, yoffset):
    print(f"Scroll: {xoffset}, {yoffset}")

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Input Scroll Mouse", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_scroll_callback(window, scroll_callback)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()