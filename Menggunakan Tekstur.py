import glfw
from OpenGL.GL import *
from PIL import Image

# ... (kode inisialisasi jendela) ...

texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)

image = Image.open("tekstur.jpg")
image_data = image.tobytes("raw", "RGB", 0, -1)

glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

# ... (pengaturan parameter tekstur) ...

# ... (loop utama) ...