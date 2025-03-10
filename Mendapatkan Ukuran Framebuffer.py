import glfw

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Ukuran Framebuffer", None, None)
if not window:
    glfw.terminate()
    exit()

width, height = glfw.get_framebuffer_size(window)
print(f"Ukuran Framebuffer: {width}x{height}")

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()