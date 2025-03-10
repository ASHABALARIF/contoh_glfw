import glfw

def framebuffer_size_callback(window, width, height):
    print(f"Ukuran Framebuffer: {width}x{height}")

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Callback Ukuran Framebuffer", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()