import glfw

if not glfw.init():
    exit()

monitors = glfw.get_monitors()
for monitor in monitors:
    name = glfw.get_monitor_name(monitor)
    width, height = glfw.get_video_mode(monitor).size
    print(f"Monitor: {name}, Resolusi: {width}x{height}")

glfw.terminate()
