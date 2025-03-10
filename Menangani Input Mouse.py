import glfw

def mouse_button_callback(window, button, action, mods):
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        print("Tombol kiri mouse ditekan")

# ... (kode inisialisasi jendela) ...

glfw.set_mouse_button_callback(window, mouse_button_callback)

# ... (loop utama) ...