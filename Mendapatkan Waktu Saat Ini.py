import glfw
import time

if not glfw.init():
    exit()

window = glfw.create_window(640, 480, "Waktu GLFW", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    current_time = glfw.get_time()
    print(f"Waktu: {current_time}")
    time.sleep(1) # Menunggu 1 detik
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()