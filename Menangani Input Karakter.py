import glfw

def char_callback(window, codepoint):
    print(f"Karakter: {chr(codepoint)}")

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Input Karakter", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.set_char_callback(window, char_callback)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()