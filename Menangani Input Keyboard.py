import glfw

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# ... (kode inisialisasi jendela) ...

glfw.set_key_callback(window, key_callback)

# ... (loop utama) ...