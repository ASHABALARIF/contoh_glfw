import glfw
from PIL import Image

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Ikon Jendela", None, None)
if not window:
    glfw.terminate()
    exit()

image = Image.open("icon.png") # Membuka gambar ikon
width, height = image.size
pixels = image.tobytes("raw", "RGBA", 0, -1)

icon = glfw.Image(width, height, pixels)
glfw.set_window_icon(window, 1, icon) # Mengatur ikon jendela

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()