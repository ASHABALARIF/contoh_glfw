import glfw

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Posisi Kursor Mouse", None, None)
if not window:
    glfw.terminate()
    exit()

xpos, ypos = glfw.get_cursor_pos(window)
print(f"Posisi Kursor: {xpos}, {ypos}")

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    xpos, ypos = glfw.get_cursor_pos(window)
    print(f"Posisi Kursor: {xpos}, {ypos}")
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()